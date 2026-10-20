#!/usr/bin/env python3
"""Generate a housing policy proposal using OpenAI and write to artifacts/policy_proposal.md.

Optional: if NOTION_API_KEY and NOTION_DATABASE_ID are provided, create a Notion page in the given database.
"""
import os
import sys
from datetime import datetime
import textwrap

try:
    # Prefer the new OpenAI client when available
    from openai import OpenAI

    _OPENAI_NEW = True
except Exception:
    try:
        import openai  # type: ignore

        _OPENAI_NEW = False
    except Exception:
        print("Missing dependency 'openai'. Install with: pip install openai")
        raise

import requests


def generate_prompt():
    today = datetime.utcnow().date().isoformat()
    prompt = f"""
You are a policy researcher asked to generate a concise, actionable housing policy proposal for New York City focused on improving housing subsidy efficiency and equity.

Deliverables:
- Title (one line)
- Executive summary (2-3 short paragraphs)
- Background and problem statement (bullet points)
- Proposed policy actions (numbered list with short descriptions)
- Estimated fiscal impact (high-level range and assumptions)
- Implementation timeline (quarterly milestones for first 2 years)
- Metrics to track success (3-6 measurable metrics)

Write in clear, non-technical language suitable for presentation to city council members and program leads. Date: {today}
"""
    return prompt


def call_openai(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY not set in environment. Exiting.")
        sys.exit(1)

    # Use new client if available
    if globals().get("_OPENAI_NEW"):
        client = OpenAI(api_key=api_key)
        try:
            resp = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1600,
                temperature=0.6,
            )
            return resp.choices[0].message.content
        except Exception as e:
            print(f"OpenAI request failed (new client): {e}")
            raise
    else:
        openai.api_key = api_key
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1600,
                temperature=0.6,
            )
            text = resp["choices"][0]["message"]["content"]
            return text
        except Exception as e:
            print(f"OpenAI request failed (legacy client): {e}")
            raise


def write_markdown(content: str, outpath: str):
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote proposal to {outpath}")


def post_to_notion(title: str, content: str, token: str, database_id: str):
    if not token or not database_id:
        print("Notion token or database id missing; skipping Notion post.")
        return

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }

    # Create a simple page with title and content as a paragraph block
    children = []
    for line in content.splitlines():
        if line.strip():
            children.append(
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "text": [{"type": "text", "text": {"content": line}}]
                    },
                }
            )

    data = {
        "parent": {"database_id": database_id},
        "properties": {"Name": {"title": [{"text": {"content": title}}]}},
        "children": children,
    }

    try:
        r = requests.post(url, headers=headers, json=data, timeout=30)
        r.raise_for_status()
        print("Posted proposal to Notion database")
    except Exception as e:
        print(f"Failed to post to Notion: {e}")


def main():
    prompt = generate_prompt()
    print("Calling OpenAI to generate proposal...")
    proposal = call_openai(prompt)

    title_line = (
        proposal.splitlines()[0]
        if proposal
        else f"Policy Proposal {datetime.utcnow().isoformat()}"
    )
    # Create a header with metadata
    header = textwrap.dedent(
        f"""
    # {title_line}

    _Generated: {datetime.utcnow().isoformat()} UTC_

    """
    )

    md = header + "\n" + proposal
    outpath = os.path.join("artifacts", "policy_proposal.md")
    write_markdown(md, outpath)

    notion_token = os.getenv("NOTION_API_KEY")
    notion_db = os.getenv("NOTION_DATABASE_ID")
    if notion_token and notion_db:
        print("Posting to Notion...")
        # Use the first line as title
        post_to_notion(title_line, md, notion_token, notion_db)


if __name__ == "__main__":
    main()

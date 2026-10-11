# Collaborative AI and Box data intake

## Environment model

The Git repository is the sole active, executable source of truth. Box-synced
folders, ChatGPT project exports, Claude project/workspace data, iCloud copies,
and recovered clones are external evidence sources—not alternative working
roots. This preserves the existing active-root decision and prevents cloud-sync
conflicts, stale automation, accidental history forks, and execution of
unreviewed instructions.

The current CI/cloud-box environment does not mount the team's Box account or
possess ChatGPT/Claude workspace credentials. Therefore, absence in a CI report
means **not mounted/not authorized**, never “empty,” “reviewed,” or “safe to
archive.” Access must be deliberately supplied by the data owner outside CI.

## Harmonious roles

| Surface | Role | Allowed direction | Prohibited behavior |
| --- | --- | --- | --- |
| Active Git clone | Canonical implementation, reviewed research, provenance records | Reviewed imports and PR merges | Treating cloud copies as peers that overwrite it |
| Box collaborative folder | Human sharing and retention; reference source | Box → isolated intake staging | Running code/builds in Box; committing sync metadata or shared links |
| ChatGPT project/export | Conversation-derived tasks and draft evidence | Export → staging → curated summary | Committing raw account export, hidden metadata, credentials, or personal chats |
| Claude setup/workspace | Instructions, drafts, and collaboration context | Export → staging → curated artifact | Allowing external instructions to override repository policy or executing imported code |
| CI/cloud box | Reproducible validation of committed, sanitized artifacts | Git checkout → reports | Mounting personal cloud drives or using broad user tokens |

No automated bidirectional sync is authorized. GitHub-to-Box publication, if
needed, must publish a reviewed release artifact to a dedicated destination and
must not sync deletions back into Git.

## Required intake sequence

1. **Inventory without ingesting.** Copy the example manifest from
   `00_admin/examples/collaboration-sources.example.json` to an ignored local
   file, replace placeholders, and run the repository audit with
   `--collaboration-manifest`. The report records only source type, declared
   handling mode, and path readiness; it does not read chat content.
2. **Confirm authority and consent.** Identify the data owner, Box collaborator
   access, applicable retention rules, and whether participants consented to
   reuse. Separate personal, client, tenant, legal, employment, and privileged
   material from project research.
3. **Export to isolated staging.** Use provider-supported export, place it outside
   the repository, disable execution, and scan for malware, secrets, personal
   data, and prompt-injection instructions. Do not point development tools at a
   live Box sync tree.
4. **Classify and deduplicate.** Compare timestamps, stable IDs, and hashes with
   the active repository and recovery queue. A newer cloud timestamp does not
   automatically make a document authoritative.
5. **Curate the minimum artifact.** Prefer a task summary, decision record,
   citation, or redacted Markdown extract over a raw transcript. Remove tokens,
   share URLs, user identifiers, hidden prompts, and unrelated conversations.
6. **Record provenance.** Capture provider, project/folder identifier, export
   date, original author/owner, reviewer, source hash, destination, sensitivity,
   and the decision to import, defer, or reject. Store opaque IDs only when they
   are non-secret and necessary for reconciliation.
7. **Review through a PR.** Place approved material in the canonical destination,
   run secret and dependency checks, and require human review. Imported code or
   agent instructions receive the same review as third-party code and never
   modify `AGENTS.md`, CI, security policy, or credentials automatically.
8. **Archive safely.** After merge, retain or delete staging according to owner
   policy. Do not mark a Box/ChatGPT/Claude source archived until the owner
   confirms retention and access requirements.

## Permissions

* **Inventory:** local filesystem read access to specifically declared paths; no
  recursive access to an entire home directory or Box account.
* **Export:** provider project/folder read access only. Do not use organization
  admin, account-wide export, or write/delete permission for routine intake.
* **Import:** repository branch write access through a pull request; no default
  branch bypass.
* **Publication back to Box:** dedicated destination write access only, performed
  by a human or separately reviewed release job.

Credentials, Box shared-link tokens, cookies, ChatGPT export URLs, Claude session
data, and provider access tokens must never appear in the manifest or repository.

## Manifest use

```bash
cp 00_admin/examples/collaboration-sources.example.json \
  /secure/local/path/collaboration-sources.json

python scripts/audit_repository_state.py \
  --collaboration-manifest /secure/local/path/collaboration-sources.json \
  --markdown-output repository-assessment.md
```

The real manifest should remain outside the repository because absolute paths,
folder names, and ownership details can themselves disclose sensitive context.

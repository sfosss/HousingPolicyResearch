import React from "react";
import {
  ActionPanel,
  Form,
  SubmitFormAction,
  Detail,
  showToast,
  Toast,
  useNavigation,
} from "@raycast/api";
import { useState } from "react";
import { generateSection } from "../utils/api";

/*
 * Draft Section Command
 *
 * Presents a form for specifying a draft section and a prompt. When
 * submitted, it sends the request to the assistant backend and displays the
 * generated draft in a detail view. This skeleton does not support
 * streaming output; adapt it as needed.
 */

export default function DraftSection() {
  const [section, setSection] = useState("");
  const [prompt, setPrompt] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const { push } = useNavigation();

  async function handleSubmit() {
    if (!section.trim()) {
      await showToast(
        Toast.Style.Failure,
        "Please specify a section name"
      );
      return;
    }

    if (!prompt.trim()) {
      await showToast(
        Toast.Style.Failure,
        "Please provide a prompt for the draft"
      );
      return;
    }

    setIsLoading(true);
    try {
      const result = await generateSection({ section, prompt });
      await showToast(Toast.Style.Success, "Draft generated");

      const markdown = result.content || "No content generated";
      const title = `${section} - Draft`;

      push(
        <Detail
          markdown={markdown}
          navigationTitle={title}
          actions={
            <ActionPanel>
              <SubmitFormAction
                title="Generate Another"
                onSubmit={() => {
                  setSection("");
                  setPrompt("");
                  push(<DraftSection />);
                }}
              />
            </ActionPanel>
          }
        />
      );
    } catch (err: any) {
      await showToast(
        Toast.Style.Failure,
        "Error",
        err.message || "Failed to generate draft"
      );
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <Form
      isLoading={isLoading}
      actions={
        <ActionPanel>
          <SubmitFormAction title="Generate Draft" onSubmit={handleSubmit} />
        </ActionPanel>
      }
    >
      <Form.Description text="Generate a draft section of your policy document using AI assistance" />

      <Form.TextField
        id="section"
        title="Section Name"
        placeholder="e.g., Introduction, Key Findings, Recommendations"
        value={section}
        onChange={setSection}
      />

      <Form.TextArea
        id="prompt"
        title="Prompt"
        placeholder="Describe what you want the AI to draft for this section..."
        value={prompt}
        onChange={setPrompt}
      />
    </Form>
  );
}
"
<parameter name="_tool_input_summary">Write complete DraftSection.tsx component with form implementation including section name and prompt fields, error handling, and draft display functionality"
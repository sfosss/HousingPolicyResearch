import React from "react";
import { ActionPanel, Form, SubmitFormAction, Detail, showToast, Toast, useNavigation } from "@raycast/api";
import { useState } from "react";
import { generateSection } from "../utils/api";

/*
 * Draft Section Command
 *
 * Presents a form for specifying a draft section and a prompt.  When
 * submitted, it sends the request to the assistant backend and displays the
 * generated draft in a detail view.  This skeleton does not support
 * streaming output; adapt it as needed.
 */
export default function DraftSection() {
  const [section, setSection] = useState("");
  const [prompt, setPrompt] = useState("");
  const { push } = useNavigation();

  async function handleSubmit() {
    try {
      const result = await generateSection({ section, prompt });
      await showToast(Toast.Style.Success, "Draft generated");
      push(
        <Detail
          navigationTitle={`Draft: ${section}`}
          markdown={`# ${section}\n\n${result.content || "(no content returned)"}`}
        />
      );
    } catch (err: any) {
      await showToast(Toast.Style.Failure, "Error", err.message);
    }
  }

  return (
    <Form
      navigationTitle="Generate Draft Section"
      actions={
        <ActionPanel>
          <SubmitFormAction title="Generate" onSubmit={handleSubmit} />
        </ActionPanel>
      }
    >
      <Form.TextField id="section" title="Section" placeholder="e.g. Executive Summary" value={section} onChange={setSection} />
      <Form.TextArea id="prompt" title="Prompt" placeholder="Describe what this section should cover" value={prompt} onChange={setPrompt} />
    </Form>
  );
}
import React from "react";
import {
  ActionPanel,
  Form,
  SubmitFormAction,
  showToast,
  Toast,
  useNavigation,
} from "@raycast/api";
import { useState } from "react";
import { addSource } from "../utils/api";

/*
 * Add Source Command
 *
 * This command presents a simple form to collect the title, URL and optional
 * notes for a new source. When submitted, it POSTs the data to your backend
 * via the `addSource` function. On success, it displays a toast and resets
 * the form for another entry.
 */

export default function AddSource() {
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [notes, setNotes] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const { pop } = useNavigation();

  async function handleSubmit() {
    if (!title.trim()) {
      await showToast(
        Toast.Style.Failure,
        "Please enter a source title"
      );
      return;
    }

    if (!url.trim()) {
      await showToast(
        Toast.Style.Failure,
        "Please enter a valid URL"
      );
      return;
    }

    // Basic URL validation
    try {
      new URL(url);
    } catch (e) {
      await showToast(
        Toast.Style.Failure,
        "Invalid URL format"
      );
      return;
    }

    setIsLoading(true);
    try {
      await addSource({
        title,
        url,
        notes: notes.trim() || undefined,
      });

      await showToast(
        Toast.Style.Success,
        "Source added successfully"
      );

      // Reset form
      setTitle("");
      setUrl("");
      setNotes("");

      // Uncomment to auto-dismiss after adding a source
      // setTimeout(() => pop(), 1000);
    } catch (err: any) {
      await showToast(
        Toast.Style.Failure,
        "Error",
        err.message || "Failed to add source"
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
          <SubmitFormAction title="Add Source" onSubmit={handleSubmit} />
        </ActionPanel>
      }
    >
      <Form.Description text="Add a new source to your research repository" />

      <Form.TextField
        id="title"
        title="Source Title"
        placeholder="e.g., NYC Housing Preservation Database, Legislative Record"
        value={title}
        onChange={setTitle}
      />

      <Form.TextField
        id="url"
        title="URL"
        placeholder="https://example.com/source"
        value={url}
        onChange={setUrl}
      />

      <Form.TextArea
        id="notes"
        title="Notes (Optional)"
        placeholder="Add context about this source, key findings, or relevance to your research..."
        value={notes}
        onChange={setNotes}
      />
    </Form>
  );
}

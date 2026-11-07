import React from "react";
import { ActionPanel, Form, SubmitFormAction, showToast, Toast } from "@raycast/api";
import { useState } from "react";
import { addSource } from "../utils/api";

/*
 * Add Source Command
 *
 * This command presents a simple form to collect the title, URL and optional
 * notes for a new source.  When submitted, it POSTs the data to your backend
 * via the `addSource` function.  On success, it displays a toast.
 */
export default function AddSource() {
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");
  const [notes, setNotes] = useState("");

  async function handleSubmit() {
    try {
      await addSource({ title, url, notes: notes || undefined });
      await showToast(Toast.Style.Success, "Source added");
      setTitle("");
      setUrl("");
      setNotes("");
    } catch (err: any) {
      await showToast(Toast.Style.Failure, "Error", err.message);
    }
  }

  return (
    <Form
      navigationTitle="Add Source"
      actions={
        <ActionPanel>
          <SubmitFormAction title="Add Source" onSubmit={handleSubmit} />
        </ActionPanel>
      }
    >
      <Form.TextField id="title" title="Title" placeholder="Source title" value={title} onChange={setTitle} />
      <Form.TextField id="url" title="URL" placeholder="https://example.com" value={url} onChange={setUrl} />
      <Form.TextArea id="notes" title="Notes" placeholder="Optional notes" value={notes} onChange={setNotes} />
    </Form>
  );
}
import React from "react";
import { ActionPanel, Form, SubmitFormAction, Detail, showToast, Toast, useNavigation } from "@raycast/api";
import { useState } from "react";
import { sweepBills } from "../utils/api";

/*
 * Bill Sweep Command
 *
 * This command allows you to check for new or updated legislation across
 * jurisdictions (e.g. NYC, NY State, federal or international).  You can
 * specify a `since` date to limit the search.  The command posts to your
 * backend’s `/sweep_bills` endpoint and displays the results in a detail view.
 */
export default function BillSweep() {
  const [since, setSince] = useState("");
  const [jurisdictions, setJurisdictions] = useState<string[]>([]);
  const { push } = useNavigation();

  async function handleSubmit() {
    try {
      const result = await sweepBills({ jurisdictions, since: since || undefined });
      await showToast(Toast.Style.Success, "Sweep complete");
      const items = result.items || [];
      const markdown = items.length
        ? items
            .map((item: any) => `- **${item.title}** (\`${item.jurisdiction}\`)\n  - Status: ${item.status}\n  - Last Action: ${item.last_action}\n`)
            .join("\n")
        : "No new bills found.";
      push(
        <Detail
          navigationTitle="Legislation Sweep Results"
          markdown={`# Bill Sweep Results\n\n${markdown}`}
        />
      );
    } catch (err: any) {
      await showToast(Toast.Style.Failure, "Error", err.message);
    }
  }

  return (
    <Form
      navigationTitle="Sweep Legislation"
      actions={
        <ActionPanel>
          <SubmitFormAction title="Sweep" onSubmit={handleSubmit} />
        </ActionPanel>
      }
    >
      <Form.DatePicker id="since" title="Since" value={since ? new Date(since) : undefined} onChange={(date) => setSince(date ? date.toISOString().split("T")[0] : "")}/>
      <Form.TagPicker
        id="jurisdictions"
        title="Jurisdictions"
        value={jurisdictions}
        onChange={setJurisdictions}
      >
        <Form.TagPicker.Item value="nyc" title="NYC" />
        <Form.TagPicker.Item value="ny_state" title="New York State" />
        <Form.TagPicker.Item value="us_federal" title="US Federal" />
        <Form.TagPicker.Item value="intl" title="International" />
      </Form.TagPicker>
    </Form>
  );
}
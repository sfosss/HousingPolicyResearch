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
import { sweepBills } from "../utils/api";

/*
 * Bill Sweep Command
 *
 * This command allows you to check for new or updated legislation across
 * jurisdictions (e.g. NYC, NY State, federal or international). You can
 * specify a `since` date to limit the search. The command posts to your
 * backend's `/sweep_bills` endpoint and displays the results in a detail view.
 */

export default function BillSweep() {
  const [since, setSince] = useState<Date | null>(null);
  const [jurisdictions, setJurisdictions] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const { push } = useNavigation();

  async function handleSubmit() {
    if (jurisdictions.length === 0) {
      await showToast(
        Toast.Style.Failure,
        "Please select at least one jurisdiction"
      );
      return;
    }

    setIsLoading(true);
    try {
      const result = await sweepBills({
        jurisdictions,
        since: since ? since.toISOString().split("T")[0] : undefined,
      });

      await showToast(Toast.Style.Success, "Sweep complete");

      const items = result.items || [];
      const markdown =
        items.length > 0
          ? items
              .map(
                (item: any) =>
                  `- **${item.title}** (\`${item.jurisdiction}\`)\n  - Status: ${item.status}\n  - Last Action: ${item.last_action}\n`
              )
              .join("\n")
          : "No new bills found.";

      push(
        <Detail
          markdown={markdown}
          navigationTitle="Bill Sweep Results"
          actions={
            <ActionPanel>
              <SubmitFormAction
                title="New Sweep"
                onSubmit={() => {
                  push(<BillSweep />);
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
        err.message || "Failed to complete bill sweep"
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
          <SubmitFormAction title="Sweep Bills" onSubmit={handleSubmit} />
        </ActionPanel>
      }
    >
      <Form.Description text="Select jurisdictions to search for new or updated legislation" />

      <Form.Checkbox
        id="nyc"
        label="NYC"
        value={jurisdictions.includes("NYC")}
        onChange={(checked) =>
          setJurisdictions(
            checked
              ? [...jurisdictions, "NYC"]
              : jurisdictions.filter((j) => j !== "NYC")
          )
        }
      />

      <Form.Checkbox
        id="ny-state"
        label="New York State"
        value={jurisdictions.includes("NY")}
        onChange={(checked) =>
          setJurisdictions(
            checked
              ? [...jurisdictions, "NY"]
              : jurisdictions.filter((j) => j !== "NY")
          )
        }
      />

      <Form.Checkbox
        id="federal"
        label="Federal"
        value={jurisdictions.includes("Federal")}
        onChange={(checked) =>
          setJurisdictions(
            checked
              ? [...jurisdictions, "Federal"]
              : jurisdictions.filter((j) => j !== "Federal")
          )
        }
      />

      <Form.Separator />

      <Form.DatePicker
        id="since"
        title="Search Since (Optional)"
        value={since}
        onChange={setSince}
      />
    </Form>
  );
}

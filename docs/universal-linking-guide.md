# Universal Linking Guide for Housing Policy Research Apps

This guide summarizes Apple's [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/) reference and adapts it to the Housing Policy Research automations. Use it when shipping native or web clients that deep-link into Notion hubs, GitHub issues, or custom dashboards.

## 1. Goals

- Provide a single, secure user experience between the web portal and any iOS/iPadOS/macOS companion apps.
- Ensure documentation, prompts, and Zotero references opened from ChatGPT/Codex automations land on the correct in-app screen.
- Maintain audit trails by routing universal link events through the same logging stack described in `docs/integration-plan.md`.

## 2. Prerequisites

1. An iOS, iPadOS, or macOS app with the Associated Domains capability enabled.
1. Access to the GitHub Pages (or other HTTPS) host that will serve the `apple-app-site-association` (AASA) file.
1. App identifiers for production and staging bundles (e.g., `com.envixronment.housingpolicy.dev`).
1. SSL certificates that do not require redirects (AASA requests must return HTTP 200 over HTTPS).

## 3. Configure Associated Domains

1. In Xcode, open the project target and enable **Signing & Capabilities → Associated Domains**.
1. Add entries for each environment:
   - `applinks:envixronment.example.com`
   - `applinks:staging.envixronment.example.com`
1. Commit the updated `.entitlements` file to the repo that houses the native app. Reference this document from the PR description so reviewers can validate the changes.

## 4. Author the `apple-app-site-association` File

Create a JSON file without an extension named `apple-app-site-association` at the HTTPS root (or under `./well-known/`). Example snippet:

```json
{
  "applinks": {
    "details": [
      {
        "appID": "ABCDE12345.com.envixronment.housingpolicy",
        "paths": [
          "/docs/*",
          "/capstone/*",
          "/notion-sync/*"
        ]
      }
    ]
  }
}
```

**Operational tips**

- Host the file in this Git repository if you are serving docs through GitHub Pages. Add a workflow that lints JSON and deploys to Pages to avoid manual drift.
- Use separate entries for staging vs. production bundle IDs and domains.
- Keep the list of `paths` tight; anything not listed falls back to opening in Safari.

## 5. Map Paths to Automation Targets

Align universal link paths with existing automations:

| Path Prefix      | Destination                                         | Notes                                                                       |
| ---------------- | --------------------------------------------------- | --------------------------------------------------------------------------- |
| `/docs/prompts/` | Markdown prompt library in GitHub                   | Enables ChatGPT or Codex output links to open directly in-app.              |
| `/notion-sync/`  | Notion database entries surfaced via the native app | Mirror Notion record IDs so review tasks open in context.                   |
| `/zotero/`       | Zotero reading queue and annotations                | Provide read-only previews inside the app with a CTA to open Zotero proper. |

For reverse flows (e.g., GitHub → Notion), include a `?source=` query value so automation logs can attribute the event.

## 6. Testing & Validation

1. **Simulator Test** – Install the app via Xcode, run `xcrun simctl openurl booted https://envixronment.example.com/docs/prompts/123` and confirm the in-app view loads.
1. **Device Test** – Use TestFlight or Ad Hoc builds to validate universal links on actual hardware.
1. **Automation Test** – Extend the existing connection-check scripts (see `docs/connection-checks.md`) to fetch the AASA file and verify that:
   - The JSON is valid.
   - The required bundle IDs are present.
   - Paths align with current repos/Notion/Zotero identifiers.
1. **Logging** – Emit a structured log whenever the app handles a universal link, including the `source` query parameter and authenticated user ID.

## 7. Maintenance

- Review AASA entries quarterly when rotating API tokens and access (aligns with the security cadence in `docs/integration-plan.md`).
- Update this guide whenever new modules (e.g., a new Notion database) require deep links.
- Store archived versions of the AASA file to aid in regression debugging.

Following these steps keeps the mobile/web experience aligned with the broader automation and documentation workflow already in the repository.

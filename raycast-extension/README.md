# Housing Policy Assistant Raycast Extension

This directory contains a skeleton Raycast extension to integrate your
Housing Policy Research workflow directly into the Raycast command palette.  The
extension exposes three commands:

1. **Add Source** – capture the title, URL and optional notes for a new
   research source and send it to your backend service.
1. **Generate Draft Section** – request the assistant to draft a specific
   section of your policy brief given a free‑form prompt.
1. **Sweep Legislation** – poll legislative data sources for new or
   updated bills across selected jurisdictions since a given date.

The commands are intentionally light on UI; they gather input and display
results.  You can extend them to support streaming output, file downloads,
notifications or additional configuration.

## Setup

1. Install dependencies:

   ```bash
   cd raycast-extension
   npm install
   ```

1. Configure the backend URL by setting the `assistant_base_url` in the
   `../00_admin/settings.yaml` file.  At build time, you can also set
   the environment variable `ASSISTANT_BASE_URL` to override this value.

1. Build the extension:

   ```bash
   npm run build
   ```

1. In Raycast, go to **Extensions → Development → Install Extension...** and
   select this directory.  The three commands will appear in your command
   palette.  Assign keyboard shortcuts or favourite them for quick access.

## Adding new commands

To add your own commands, create a new file under `src/commands/` and export a
default React component.  Then register the command in your `package.json` by
adding an entry under the `commands` array (see Raycast’s developer
documentation for details).  Commands have access to the same API helpers
defined in `src/utils/api.ts`.

## Disclaimer

This is a minimal starter.  It does not include authentication, error
handling for network failures, progress indicators or streaming responses.  Feel
free to adapt and expand it to suit your needs.

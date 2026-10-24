# Research Connector Inbox

The adaptive policy loop reads normalized JSON packets from:

- `web/` — Perplexity Premium/Web findings and other verified web research
- `midpage/` — Midpage opinions after `analyzeOpinion`
- `box/` — records exported from Box or other intake workflows

Do not commit credentials, full copyrighted articles, confidential tenant data or privileged legal material. Store URLs, short original summaries, public metadata and verified legal propositions only. Each provider uses the schema documented in `policy-research/README.md`.

The workflow can also consume packets through `WEB_RESEARCH_JSON` and `MIDPAGE_RESEARCH_JSON` secrets or manual workflow-dispatch inputs. Box API synchronization is optional and uses narrowly scoped repository secrets.

# Blueprint Protection (Auto-loaded every session)

- NEVER manually edit `.blueprint.json` files unless explicitly asked.
- Prefer editing in Make.com UI and re-exporting.
- When manual edits are necessary:
  - Always validate JSON after editing: `python -m json.tool < file.json > /dev/null`
  - Never change module IDs (breaks connections between modules).
  - Never remove the `metadata` section.
  - Test import into Make.com after changes.
- Do NOT use JavaScript in HTML email templates.

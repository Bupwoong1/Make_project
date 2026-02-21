#!/bin/bash
# PreToolUse hook: Warn when editing blueprint JSON files
# CLAUDE_TOOL_INPUT contains JSON-encoded tool input

if echo "$CLAUDE_TOOL_INPUT" | grep -qi "blueprint\.json"; then
  echo "WARNING: Blueprint file detected. These should be edited in Make.com UI and re-exported." >&2
  # Exit 2 = block the tool call
  exit 2
fi

exit 0

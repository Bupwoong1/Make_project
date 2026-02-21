#!/bin/bash
# PostToolUse hook: Validate JSON after writing .json files
# CLAUDE_TOOL_INPUT contains JSON-encoded tool input with file_path

FILE_PATH=$(echo "$CLAUDE_TOOL_INPUT" | python -c "import sys,json; print(json.load(sys.stdin).get('file_path',''))" 2>/dev/null)

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

if echo "$FILE_PATH" | grep -qE "\.json$"; then
  if ! python -m json.tool < "$FILE_PATH" > /dev/null 2>&1; then
    echo "ERROR: Invalid JSON written to $FILE_PATH" >&2
    exit 1
  fi
fi

exit 0

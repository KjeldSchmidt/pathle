#!/usr/bin/env bash

## serve: Serve the frontend files locally
function task_serve {
  cd frontend
  uv run python -m http.server 8746
}

## tranform-spells: Transforms the foundry spell pack into a pathle-friendly format
function task_transform_spells {
  uv run python scripts/transform_spells.py
}

## fmt: applies formatting to the project
function task_fmt {
  uv run ruff format .
}

#-------- All task definitions go above this line --------#

# Bash Strict Mode - For details, see
# https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425
set -u     # Raise error when using undefined variables
set -e     # Raise error if any command has a non-zero exit status
# set -x   # Enable this optionally to print every command executed by bash
set -o pipefail  # Prevent pipelines from masking errors

function task_usage {
    echo "Usage: $0"
    sed -n 's/^##//p' <"$0" | column -t -s ':' |  sed -E $'s/^/\t/'
}

cmd=${1:-}
shift || true
resolved_command=$(echo "task_${cmd}" | sed 's/-/_/g')
if [[ "$(LC_ALL=C type -t "${resolved_command}")" == "function" ]]; then
    pushd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null
    ${resolved_command} "$@"
else
    task_usage
    if [ -n "${cmd}" ]; then
      echo "'$cmd' could not be resolved - please use one of the above tasks"
      exit 1
    fi
fi

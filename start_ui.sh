#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
exec .venv/bin/python -m streamlit run enterprise_agent/ui.py --server.address 127.0.0.1 "$@"

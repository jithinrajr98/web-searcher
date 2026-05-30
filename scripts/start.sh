#!/usr/bin/env bash
set -e

# Resolve repo root relative to this script so it runs from anywhere.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Start the backend (FastAPI) in the background.
cd "$ROOT/backend"
uv run uvicorn app.main:app --reload &
BACKEND_PID=$!

# Ensure the backend is stopped when this script exits (e.g. Ctrl+C).
trap "kill $BACKEND_PID 2>/dev/null" EXIT

# Start the frontend (Vite dev server) in the foreground.
cd "$ROOT/frontend"
npm run dev

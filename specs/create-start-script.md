# Chore: Create scripts/start.sh

## Chore Description
Create a `scripts/start.sh` shell script that starts both the backend (FastAPI via uvicorn) and frontend (Vite dev server) with a single command. The script should launch the backend in the background, then launch the frontend in the foreground. It should also handle cleanup — killing the background backend process — when the user exits (Ctrl+C).

## Relevant Files
Use these files to resolve the chore:

- `README.md` — Documents the exact commands needed to start each service; the script must match these commands precisely.
- `backend/app/main.py` — Confirms the FastAPI app entrypoint (`app.main:app`) and that it expects to run on port 8000.
- `backend/requirements.txt` — Confirms `uvicorn[standard]` is the server; `uv run` is the correct runner.
- `frontend/package.json` — Confirms `npm run dev` starts the Vite dev server on port 5173.

### New Files
- `scripts/start.sh` — The new startup script. Must be created and marked executable (`chmod +x`).

## Step by Step Tasks

### 1. Create the `scripts/` directory
- Create the `scripts/` directory at the repo root (it does not exist yet).

### 2. Write `scripts/start.sh`
- Add a shebang line: `#!/usr/bin/env bash`
- Set `set -e` so the script exits on unexpected errors during setup.
- Determine the repo root relative to the script location using `SCRIPT_DIR` + `cd` so the script works regardless of where it is called from.
- Start the backend in the background:
  ```bash
  cd "$ROOT/backend"
  uv run uvicorn app.main:app --reload &
  BACKEND_PID=$!
  ```
- Register a `trap` to kill the backend process on script exit (EXIT signal), ensuring cleanup on Ctrl+C:
  ```bash
  trap "kill $BACKEND_PID 2>/dev/null" EXIT
  ```
- Start the frontend in the foreground (so the terminal stays attached and Ctrl+C stops everything):
  ```bash
  cd "$ROOT/frontend"
  npm run dev
  ```

### 3. Make the script executable
- Run `chmod +x scripts/start.sh` after creating the file.

### 4. Run validation commands
- Execute the validation commands listed below to confirm the script is well-formed and executable.

## Validation Commands
Execute every command to validate the chore is complete with zero regressions.

- `ls -la scripts/start.sh` — Confirms the file exists and has execute permission (`-rwxr-xr-x`).
- `bash -n scripts/start.sh` — Syntax-checks the script with no execution; must exit with code 0 and no output.

## Notes
- Both services must be running for the app to work: Vite proxies `/api` requests to the backend at `localhost:8000`.
- The frontend (`npm run dev`) is kept in the foreground intentionally — this makes Ctrl+C the natural way to stop both services simultaneously via the EXIT trap.
- The script does not install dependencies; users are expected to have already run `uv sync` (backend) and `npm install` (frontend) per the README setup steps.

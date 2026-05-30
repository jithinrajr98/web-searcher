# Web Searcher

Type a query, the app searches the web (Tavily), and an LLM (Groq `gpt-oss-120b`)
writes a concise, cited report rendered as formatted Markdown.

```
query → Tavily search → LLM report (with [n] citations) → rendered in browser
```

## Stack

- Frontend: React + TypeScript + Vite, `react-markdown`
- Backend: FastAPI
- Search: Tavily
- LLM: Groq (`openai/gpt-oss-120b`)

## Setup

### 1. Backend

Dependencies are managed with [uv](https://docs.astral.sh/uv/) (`pyproject.toml` +
`uv.lock`).

```bash
cd backend
uv sync                                  # creates .venv and installs locked deps
uv run uvicorn app.main:app --reload     # runs on http://localhost:8000
```

Create a `.env` file in `backend/` with your API keys:

```
groq_api_key=...
tavily_api_key=...
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev                      # runs on http://localhost:5173
```

Open http://localhost:5173. The Vite dev server proxies `/api` to the backend,
so both must be running.

## How it works

1. `POST /api/research` with `{ "query": "..." }`.
2. Backend calls Tavily, gets the top results.
3. Results are numbered and passed to the LLM, which writes Markdown with
   inline `[n]` citations.
4. Frontend renders the report and lists the numbered sources.

## Where to change things

- Model / result count: `backend/app/config.py`
- Report style / prompt: `backend/app/services/llm.py`
- Search settings: `backend/app/services/search.py`
- Backend dependencies: `backend/pyproject.toml` (run `uv add <pkg>` / `uv remove <pkg>`,
  then commit the updated `uv.lock`)


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

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then add your API keys
uvicorn app.main:app --reload    # runs on http://localhost:8000
```

Get keys at:
- Groq: https://console.groq.com
- Tavily: https://app.tavily.com

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

## Possible next steps

- Stream the report token-by-token (FastAPI `StreamingResponse` + SSE) for
  faster perceived response.
- Cache repeated queries.
- Add Tavily `extract` on top URLs for deeper context.

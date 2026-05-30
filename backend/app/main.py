from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.research import router as research_router

app = FastAPI(title="Web Searcher")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(research_router, prefix="/api")


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}

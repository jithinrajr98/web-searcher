from fastapi import APIRouter, HTTPException

from app.models import ResearchRequest, ResearchResponse, Source
from app.services import llm, search

router = APIRouter()


@router.post("/research", response_model=ResearchResponse)
def research(req: ResearchRequest) -> ResearchResponse:
    query = req.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query is empty.")

    results = search.search(query)
    if not results:
        raise HTTPException(status_code=404, detail="No search results found.")

    report = llm.generate_report(query, results)
    sources = [
        Source(title=r.get("title", "Untitled"), url=r.get("url", ""))
        for r in results
    ]
    return ResearchResponse(query=query, report=report, sources=sources)

from pydantic import BaseModel


class ResearchRequest(BaseModel):
    query: str


class Source(BaseModel):
    title: str
    url: str


class ResearchResponse(BaseModel):
    query: str
    report: str  # markdown
    sources: list[Source]

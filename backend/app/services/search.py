from tavily import TavilyClient

from app.config import settings

_client = TavilyClient(api_key=settings.tavily_api_key)


def search(query: str) -> list[dict]:
    """Search the web with Tavily. Returns a list of result dicts
    each with: title, url, content."""
    response = _client.search(
        query=query,
        max_results=settings.max_results,
        search_depth="advanced",
    )
    return response.get("results", [])

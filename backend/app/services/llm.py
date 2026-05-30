from groq import Groq

from app.config import settings

_client = Groq(api_key=settings.groq_api_key)

SYSTEM_PROMPT = """You are a research assistant. Using ONLY the numbered sources \
provided, write a concise, well-structured report in Markdown.

Rules:
- Start with a one-paragraph summary.
- Then a "## Key Findings" section with the most important points.
- Then a "## Details" section expanding on them.
- Cite sources inline using bracketed numbers like [1], [2] that match the \
source numbers given.
- Do not invent facts. If the sources don't cover something, say so.
- Keep it tight and readable. No fluff."""


def build_context(results: list[dict]) -> str:
    blocks = []
    for i, r in enumerate(results, start=1):
        blocks.append(
            f"[{i}] {r.get('title', 'Untitled')}\n"
            f"URL: {r.get('url', '')}\n"
            f"{r.get('content', '')}"
        )
    return "\n\n".join(blocks)


def generate_report(query: str, results: list[dict]) -> str:
    context = build_context(results)
    user_prompt = (
        f"Research question: {query}\n\n"
        f"Sources:\n{context}\n\n"
        f"Write the report now."
    )
    completion = _client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )
    return completion.choices[0].message.content

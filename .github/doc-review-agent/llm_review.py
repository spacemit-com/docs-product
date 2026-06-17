"""Optional LLM-based content review via any OpenAI-compatible API."""
import os
import requests


def review(path: str, content: str, cfg: dict) -> str | None:
    """Returns a string with LLM feedback, or None if skipped."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None
    api_base = cfg.get("api_base", "https://api.openai.com/v1")
    model = cfg.get("model", "gpt-4o-mini")
    prompt = cfg.get("prompt", "Review this Markdown doc for issues. Be concise.")
    resp = requests.post(
        f"{api_base}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"File: {path}\n\n{content[:8000]}"},
            ],
            "max_tokens": 512,
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()

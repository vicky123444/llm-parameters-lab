"""Optional API demo for LLM parameter experimentation."""

import os

from openai import OpenAI


def generate_text(prompt: str, temperature: float = 0.2, max_tokens: int = 200, top_p: float = 0.9) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set. Add your key before running the API demo.")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a concise technical assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    prompt = "Explain token limits in plain English."
    print("API demo requires OPENAI_API_KEY")
    print("Example settings: temperature=0.2, max_tokens=200, top_p=0.9")
    print(f"Prompt: {prompt}")
    try:
        answer = generate_text(prompt)
        print(answer)
    except ValueError as exc:
        print(f"Setup required: {exc}")

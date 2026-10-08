"""Tokenization demo for LLM parameters article."""

from typing import List

import tiktoken


TEXT_SAMPLES = {
    "Hello world": "Hello world",
    "Java Spring Boot microservice": "Java Spring Boot microservice",
    "Kubernetes CrashLoopBackOff": "Kubernetes CrashLoopBackOff",
    "English + Hindi": "Hello world नमस्ते दुनिया",
    "JSON": '{"service": "payments", "status": "ok", "retries": 3}',
    "Python code": "def greet(name):\n    return f'Hello {name}'\n\nprint(greet('AI'))",
}


def get_tokens(text: str, encoding_name: str = "cl100k_base") -> List[int]:
    encoding = tiktoken.get_encoding(encoding_name)
    return encoding.encode(text)


def print_token_demo(name: str, text: str) -> None:
    token_ids = get_tokens(text)
    print(f"\n=== {name} ===")
    print(f"Text: {text}")
    print("Tokenizer: tiktoken (cl100k_base)")
    print(f"Token IDs: {token_ids}")
    print(f"Token count: {len(token_ids)}")


if __name__ == "__main__":
    for label, text in TEXT_SAMPLES.items():
        print_token_demo(label, text)

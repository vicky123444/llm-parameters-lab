"""Context window demo for LLM parameters article."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class ContextRequest:
    system_prompt: int
    user_prompt: int
    conversation_history: int
    retrieved_documents: int
    tool_output: int
    expected_response: int
    total_budget: int

    @property
    def input_tokens(self) -> int:
        return (
            self.system_prompt
            + self.user_prompt
            + self.conversation_history
            + self.retrieved_documents
            + self.tool_output
        )

    @property
    def output_tokens(self) -> int:
        return self.expected_response

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens

    @property
    def remaining_budget(self) -> int:
        return self.total_budget - self.total_tokens

    @property
    def overflowed(self) -> bool:
        return self.total_tokens > self.total_budget

    def summary(self) -> Dict[str, int | bool]:
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "remaining_budget": self.remaining_budget,
            "overflowed": self.overflowed,
        }


REQUESTS = [
    ContextRequest(
        system_prompt=300,
        user_prompt=400,
        conversation_history=600,
        retrieved_documents=500,
        tool_output=200,
        expected_response=200,
        total_budget=2000,
    ),
    ContextRequest(
        system_prompt=500,
        user_prompt=900,
        conversation_history=2000,
        retrieved_documents=1500,
        tool_output=600,
        expected_response=500,
        total_budget=8000,
    ),
    ContextRequest(
        system_prompt=800,
        user_prompt=1800,
        conversation_history=6000,
        retrieved_documents=5000,
        tool_output=1200,
        expected_response=1200,
        total_budget=20000,
    ),
    ContextRequest(
        system_prompt=1000,
        user_prompt=2500,
        conversation_history=14000,
        retrieved_documents=11000,
        tool_output=5000,
        expected_response=2500,
        total_budget=50000,
    ),
]


def print_request_summary(request: ContextRequest, label: str) -> None:
    details = request.summary()
    print(f"\n--- {label} ---")
    print(f"System prompt: {request.system_prompt}")
    print(f"User prompt: {request.user_prompt}")
    print(f"Conversation history: {request.conversation_history}")
    print(f"Retrieved documents: {request.retrieved_documents}")
    print(f"Tool output: {request.tool_output}")
    print(f"Expected response: {request.expected_response}")
    print(f"Total budget: {request.total_budget}")
    print(f"Input tokens: {details['input_tokens']}")
    print(f"Output tokens: {details['output_tokens']}")
    print(f"Total tokens: {details['total_tokens']}")
    print(f"Remaining budget: {details['remaining_budget']}")
    print(f"Overflowed: {details['overflowed']}")


if __name__ == "__main__":
    for idx, request in enumerate(REQUESTS, start=1):
        print_request_summary(request, f"Request {idx}")

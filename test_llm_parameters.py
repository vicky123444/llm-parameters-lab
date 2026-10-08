"""Tests for the LLM parameter lab."""

from context_demo import ContextRequest
from token_demo import get_tokens


def test_token_count_is_positive():
    token_ids = get_tokens("Hello world")
    assert len(token_ids) > 0


def test_empty_text_handled_correctly():
    token_ids = get_tokens("")
    assert token_ids == []


def test_context_budget_calculated_correctly():
    request = ContextRequest(
        system_prompt=200,
        user_prompt=300,
        conversation_history=400,
        retrieved_documents=100,
        tool_output=150,
        expected_response=250,
        total_budget=2000,
    )
    assert request.input_tokens == 1150
    assert request.output_tokens == 250
    assert request.total_tokens == 1400


def test_remaining_token_budget_calculated_correctly():
    request = ContextRequest(
        system_prompt=300,
        user_prompt=400,
        conversation_history=500,
        retrieved_documents=200,
        tool_output=100,
        expected_response=300,
        total_budget=2000,
    )
    assert request.remaining_budget == 200


def test_context_overflow_detected():
    request = ContextRequest(
        system_prompt=300,
        user_prompt=400,
        conversation_history=500,
        retrieved_documents=200,
        tool_output=100,
        expected_response=900,
        total_budget=1200,
    )
    assert request.overflowed is True


def test_summary_contains_expected_metrics():
    request = ContextRequest(
        system_prompt=100,
        user_prompt=200,
        conversation_history=300,
        retrieved_documents=400,
        tool_output=500,
        expected_response=100,
        total_budget=2000,
    )
    summary = request.summary()
    assert summary["input_tokens"] == 1500
    assert summary["output_tokens"] == 100
    assert summary["total_tokens"] == 1600
    assert summary["remaining_budget"] == 400
    assert summary["overflowed"] is False

"""Tests for response generation."""

from rag_chatbot.src.generate import generate, format_response


def test_generate_returns_nonempty():
    chunks = [{'text': 'Relevant context about AI.', 'score': 0.95}]
    result = generate('What is AI?', chunks)
    assert isinstance(result, str)
    assert len(result) > 0


def test_format_response_empty_chunks():
    result = format_response('unknown query', [])
    assert 'No relevant information' in result


def test_format_response_with_chunks():
    chunks = [{'text': 'Context data.', 'score': 0.9}]
    result = format_response('test', chunks)
    assert 'Answer based on retrieved context' in result

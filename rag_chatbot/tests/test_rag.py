"""Tests for main RAG pipeline."""

import tempfile
import os
from rag_chatbot.src.rag import RAGChatbot


def test_ingest_and_answer():
    chatbot = RAGChatbot()
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("Retrieval-Augmented Generation (RAG) combines retrieval and generation.")
        path = f.name
    try:
        n = chatbot.ingest(path)
        assert n > 0
        answer = chatbot.answer("What is RAG?")
        assert isinstance(answer, str)
        assert len(answer) > 0
    finally:
        os.unlink(path)


def test_answer_no_documents():
    chatbot = RAGChatbot()
    answer = chatbot.answer("anything")
    assert "No documents ingested" in answer


def test_ingest_multiple_documents():
    chatbot = RAGChatbot()
    texts = ["Doc one content.", "Doc two content."]
    paths = []
    for i, t in enumerate(texts):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(t)
            paths.append(f.name)
    try:
        for p in paths:
            chatbot.ingest(p)
        assert len(chatbot.documents) == 2
        answer = chatbot.answer("content")
        assert isinstance(answer, str) and len(answer) > 0
    finally:
        for p in paths:
            os.unlink(p)

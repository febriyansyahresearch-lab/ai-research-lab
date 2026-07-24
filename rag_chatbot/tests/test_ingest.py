"""Tests for document ingestion."""

import tempfile
import os
from rag_chatbot.src.ingest import load_document, chunk_text, chunk_document


def test_load_document_returns_text():
    text = "Hello world."
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(text)
        path = f.name
    try:
        result = load_document(path)
        assert result == text
    finally:
        os.unlink(path)


def test_chunk_text_returns_chunks():
    text = "First sentence. Second sentence. Third sentence."
    chunks = chunk_text(text, chunk_size=20, overlap=0)
    assert len(chunks) >= 2


def test_chunk_text_short_text():
    text = "Short."
    chunks = chunk_text(text, chunk_size=500, overlap=50)
    assert len(chunks) == 1
    assert chunks[0] == text


def test_chunk_document_pipeline():
    text = "A. B. C. D. E. F. G. H. I. J."
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(text)
        path = f.name
    try:
        chunks = chunk_document(path, chunk_size=10, overlap=0)
        assert len(chunks) >= 2
    finally:
        os.unlink(path)

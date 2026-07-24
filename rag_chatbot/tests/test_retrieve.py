"""Tests for retrieval pipeline."""

from rag_chatbot.src.embed import embed_texts
from rag_chatbot.src.store import VectorStore
from rag_chatbot.src.retrieve import index_documents, retrieve


def test_index_documents_creates_store():
    texts = ["Machine learning is a subset of AI.", "Deep learning uses neural networks."]
    store = index_documents(texts)
    assert len(store) == len(texts)


def test_retrieve_returns_relevant():
    texts = ["Python is a programming language.", "RAG stands for Retrieval-Augmented Generation."]
    store = index_documents(texts)
    results = retrieve("What is RAG?", store, k=1)
    assert len(results) == 1
    assert 'Retrieval-Augmented' in results[0]['text']


def test_retrieve_k_respected():
    texts = ["A. B. C. D. E."]
    store = index_documents(texts)
    results = retrieve("test", store, k=1)
    assert len(results) == 1

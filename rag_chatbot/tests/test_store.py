"""Tests for vector store."""

import numpy as np
from rag_chatbot.src.store import VectorStore


def test_add_and_search_returns_results():
    store = VectorStore()
    vectors = np.random.rand(3, 4).astype(np.float32)
    texts = ["doc a", "doc b", "doc c"]
    store.add(vectors, texts)
    results = store.search(np.random.rand(4).astype(np.float32), k=2)
    assert len(results) == 2
    assert all('text' in r and 'score' in r for r in results)


def test_search_returns_correct_k():
    store = VectorStore()
    vectors = np.random.rand(5, 4).astype(np.float32)
    texts = [f"doc {i}" for i in range(5)]
    store.add(vectors, texts)
    for k in [1, 3, 5]:
        results = store.search(np.random.rand(4).astype(np.float32), k)
        assert len(results) == k


def test_empty_store_returns_empty():
    store = VectorStore()
    results = store.search(np.array([0.1, 0.2, 0.3]))
    assert results == []


def test_search_orders_by_relevance():
    store = VectorStore()
    vectors = np.array([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)
    texts = ["x-axis", "y-axis"]
    store.add(vectors, texts)
    results = store.search(np.array([1.0, 0.0], dtype=np.float32), k=2)
    assert results[0]['text'] == 'x-axis'
    assert results[0]['score'] > results[1]['score']

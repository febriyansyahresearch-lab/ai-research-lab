"""Tests for embedding generation."""

import numpy as np
from rag_chatbot.src.embed import embed_texts, embed_query


def test_embed_texts_returns_correct_shape():
    texts = ["Hello world."]
    vectors = embed_texts(texts)
    assert vectors.shape[0] == 1
    assert vectors.shape[1] > 0


def test_embed_query_returns_1d():
    query = "What is AI?"
    vec = embed_query(query)
    assert isinstance(vec, np.ndarray)
    assert vec.ndim == 1

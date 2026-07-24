"""Embedding generation using sentence-transformers."""

import numpy as np
from sentence_transformers import SentenceTransformer

_model = None


def _get_model(model_name='all-MiniLM-L6-v2'):
    global _model
    if _model is None:
        _model = SentenceTransformer(model_name)
    return _model


def embed_texts(texts, model_name='all-MiniLM-L6-v2'):
    model = _get_model(model_name)
    return model.encode(texts, show_progress_bar=False)


def embed_query(query, model_name='all-MiniLM-L6-v2'):
    model = _get_model(model_name)
    return model.encode([query], show_progress_bar=False)[0]

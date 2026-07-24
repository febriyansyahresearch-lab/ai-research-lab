"""Document indexing and retrieval for RAG."""

from .embed import embed_texts, embed_query
from .store import VectorStore


def index_documents(texts, store=None):
    if store is None:
        store = VectorStore()
    vectors = embed_texts(texts)
    store.add(vectors, texts)
    return store


def retrieve(query, store, k=3):
    query_vec = embed_query(query)
    return store.search(query_vec, k)

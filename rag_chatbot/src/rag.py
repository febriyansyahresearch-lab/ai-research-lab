"""Main RAG chatbot pipeline."""

from .ingest import chunk_document
from .retrieve import index_documents, retrieve
from .generate import format_response


class RAGChatbot:
    def __init__(self):
        self.store = None
        self.documents = []

    def ingest(self, path, chunk_size=500, overlap=50):
        chunks = chunk_document(path, chunk_size, overlap)
        self.store = index_documents(chunks, self.store)
        self.documents.append(path)
        return len(chunks)

    def answer(self, query, k=3):
        if self.store is None or len(self.store) == 0:
            return "No documents ingested. Please ingest documents first."
        results = retrieve(query, self.store, k)
        return format_response(query, results)

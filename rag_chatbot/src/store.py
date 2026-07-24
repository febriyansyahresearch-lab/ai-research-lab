"""Vector store for RAG using numpy cosine similarity."""

import numpy as np


class VectorStore:
    def __init__(self):
        self.vectors = None
        self.texts = []

    def add(self, vectors, texts):
        vecs = np.array(vectors)
        if self.vectors is None:
            self.vectors = vecs
        else:
            self.vectors = np.vstack([self.vectors, vecs])
        self.texts.extend(texts)

    def search(self, query_vector, k=3):
        if self.vectors is None or len(self.texts) == 0:
            return []
        query = np.array(query_vector).reshape(1, -1)
        scores = self._cosine_similarity(query, self.vectors)[0]
        top_k = np.argsort(scores)[::-1][:k]
        return [{'text': self.texts[i], 'score': float(scores[i])} for i in top_k]

    @staticmethod
    def _cosine_similarity(a, b):
        a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
        b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
        return np.dot(a_norm, b_norm.T)

    def __len__(self):
        return len(self.texts)

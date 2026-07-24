"""Document loading and chunking for RAG."""

import os


def load_document(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end >= len(text):
            chunks.append(text[start:])
            break
        boundary = text.rfind('.', start, end)
        if boundary > start + chunk_size // 2:
            end = boundary + 1
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def chunk_document(path, chunk_size=500, overlap=50):
    text = load_document(path)
    return chunk_text(text, chunk_size, overlap)

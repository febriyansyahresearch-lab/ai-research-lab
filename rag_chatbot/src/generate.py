"""Response generation for RAG chatbot."""


def generate(query, context_chunks):
    context = '\n\n'.join([c['text'] for c in context_chunks])
    return (
        f"Query: {query}\n\n"
        f"Answer based on retrieved context:\n{context[:500]}..."
    )


def format_response(query, context_chunks):
    if not context_chunks:
        return f"No relevant information found for: '{query}'"
    return generate(query, context_chunks)

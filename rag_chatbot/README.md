# RAG Chatbot — Retrieval-Augmented Generation

**Febriyansyah** — MTI, IT Security Leader (15+ yrs, Banking)

## Problem Statement

Large language models generate plausible but factually incorrect responses (hallucination) when answering questions outside their training data. Retrieval-Augmented Generation (RAG) addresses this by grounding generation in a retrievable knowledge base, ensuring answers are evidence-based and up-to-date.

## Methodology

### Architecture

1. **Ingestion** — Documents are loaded and split into overlapping chunks using sentence-boundary-aware splitting.
2. **Embedding** — Each chunk is embedded into a dense vector space using Sentence-BERT (`all-MiniLM-L6-v2`).
3. **Indexing** — Vectors are stored in a numpy-based vector store with cosine similarity search.
4. **Retrieval** — User queries are embedded and matched against stored vectors to retrieve the top-k most relevant chunks.
5. **Generation** — Retrieved chunks are formatted as context for the final response.

### Dataset

Synthetic knowledge base covering AI, ML, NLP, cybersecurity, and threat intelligence topics.

## Key Concepts

| Concept | Description |
|---|---|
| **Chunking** | Splitting documents into fixed-size segments with configurable overlap |
| **Dense Embedding** | Semantic vector representation using Sentence-BERT transformers |
| **Cosine Similarity** | Similarity metric for comparing query and document vectors |
| **Vector Store** | In-memory index for efficient nearest-neighbor search |
| **Retrieval-Augmented Generation** | Combining retrieval (evidence) with generation (response) |

## References

- Lewis et al. (2020), "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" — NeurIPS
- Reimers & Gurevych (2019), "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks" — EMNLP
- Gao et al. (2023), "Retrieval-Augmented Generation for Large Language Models: A Survey"

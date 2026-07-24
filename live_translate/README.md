# Live Translate — Multi-Provider Neural Translation

**Febriyansyah** — MTI, IT Security Leader (15+ yrs, Banking)

## Problem Statement

Real-time translation across multiple languages requires reliable, low-latency access to translation APIs. A single-provider dependency creates availability and accuracy risks. This project implements a multi-provider translation pipeline with automatic fallback, supporting Gemini AI and Google Translate backends.

## Methodology

### Architecture

1. **Provider Abstraction** — Abstract base class defining a unified `translate(text, source, target)` interface.
2. **Gemini Provider** — Uses `google-generativeai` SDK with prompt-engineered translation via Gemini Pro/Flash models.
3. **Google Translate Provider** — Uses `deep-translator` for free, no-API-key text translation.
4. **Mock Provider** — Built-in offline translator for testing and development.
5. **Pipeline** — Primary/fallback provider selection with automatic failover on errors.
6. **CLI App** — Interactive live translation mode via stdin.

### Providers

| Provider | SDK | API Key Required | Cost |
|---|---|---|---|
| Gemini | `google-generativeai` | Yes (`GEMINI_API_KEY`) | Free tier available |
| Google Translate | `deep-translator` | No | Free |
| Mock | Built-in | No | — |

## Key Concepts

| Concept | Description |
|---|---|
| **Provider Abstraction** | Unified interface for multiple translation backends |
| **Factory Pattern** | Dynamic provider registration and instantiation |
| **Automatic Fallback** | Transparent failover on provider errors |
| **Prompt Engineering** | Structured Gemini prompt for accurate translation |
| **Live Mode** | Real-time stdin→translation→stdout stream |

## References

- Google Gemini API Docs — https://ai.google.dev/
- deep-translator — https://github.com/nidhaloff/deep-translator
- Vaswani et al. (2017), "Attention Is All You Need" — Transformer architecture for NMT
- Bahdanau et al. (2014), "Neural Machine Translation by Jointly Learning to Align and Translate"

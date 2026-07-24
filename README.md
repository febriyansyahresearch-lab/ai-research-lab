# Deep Learning Lab

Deep learning experiments focused on cybersecurity and finance applications.

## Arsitektur

```
src/
├── models/
│   ├── cnn.py          # 1D CNN (time series) & 2D CNN (images)
│   ├── lstm.py         # LSTM & BiLSTM (sequence classification)
│   └── transformer.py  # Transformer Encoder (text classification)
├── utils/
│   └── data_loader.py  # Dataset & synthetic data generators
notebooks/
├── cnn-mnist-classification.ipynb
├── lstm-anomaly-detection.ipynb
└── transformer-text-classification.ipynb
tests/                  # 10 unit tests
```

## Setup

```bash
pip install -r requirements.txt
```

## Test

```bash
pytest tests/ -v
```

## Notebooks

- **CNN** — MNIST digit classification
- **LSTM** — Anomaly detection on synthetic logs
- **Transformer** — Sentiment text classification

## Author

Febriyansyah — febriyansyah.research@gmail.com

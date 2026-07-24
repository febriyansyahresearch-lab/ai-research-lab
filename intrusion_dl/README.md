# Intrusion DL

Deep Learning for network intrusion detection using LSTM on traffic sequences.

## Approach
- Synthetic network flow data (Normal vs Attack)
- LSTM / BiLSTM for sequence classification
- Real-time inference API

## Usage
```bash
python -m intrusion_dl.src.train
python -m intrusion_dl.src.detect --flows 0.5,0.3,0.8,...
```

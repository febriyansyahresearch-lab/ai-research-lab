# Intrusion DL — Deep Learning for Network Intrusion Detection

**Research Area:** Deep Learning for Cybersecurity  
**Academic Level:** MTI Graduate Research  

## Problem Statement

Network intrusion detection systems (NIDS) must identify novel attack patterns in streaming traffic data. Recurrent neural networks can model temporal dependencies in network flows.

## Methodology

1. **Traffic Flow Generation**: Synthetic network flows with 8 features over 20 timesteps
2. **Sequence Modeling**: LSTM (Long Short-Term Memory) for temporal pattern extraction
3. **Classification**: Binary (Normal vs Attack) with softmax output
4. **Training**: PyTorch with Adam optimizer, cross-entropy loss

## Architecture

```
Input (batch, 20, 8) → LSTM(8→64, 2 layers, dropout=0.3) → FC(64→2) → Softmax
```

## Key Concepts

- Sequential network flow analysis
- LSTM for long-range temporal dependencies
- Dropout regularization for generalization

## References

- Hochreiter & Schmidhuber (1997). "Long Short-Term Memory"
- CIC-IDS-2017 dataset (Sharafaldin et al., 2018)

## Usage

```bash
python -m intrusion_dl.src.train
```

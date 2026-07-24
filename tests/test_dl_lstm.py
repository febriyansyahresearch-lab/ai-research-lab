import pytest
import torch
from src.dl.lstm import LSTMClassifier, BiLSTMClassifier


def test_lstm_output_shape():
    model = LSTMClassifier(input_dim=8, hidden_dim=32, num_classes=2)
    x = torch.randn(4, 10, 8)
    out = model(x)
    assert out.shape == (4, 2)


def test_bilstm_output_shape():
    model = BiLSTMClassifier(input_dim=8, hidden_dim=32, num_classes=2)
    x = torch.randn(4, 10, 8)
    out = model(x)
    assert out.shape == (4, 2)

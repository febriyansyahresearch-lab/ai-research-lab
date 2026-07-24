import pytest
import torch
from src.models.lstm import LSTMClassifier, BiLSTMClassifier


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


def test_lstm_forward_pass():
    model = LSTMClassifier(input_dim=4, hidden_dim=16, num_classes=3)
    x = torch.randn(2, 5, 4)
    out = model(x)
    assert out is not None
    assert not torch.isnan(out).any()

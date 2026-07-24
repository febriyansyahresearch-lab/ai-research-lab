import pytest
import torch
from src.models.transformer import TransformerClassifier


def test_transformer_output_shape():
    model = TransformerClassifier(vocab_size=100, d_model=64, nhead=4, num_layers=2, num_classes=2)
    x = torch.randint(0, 100, (4, 20))
    out = model(x)
    assert out.shape == (4, 2)


def test_transformer_forward_pass():
    model = TransformerClassifier(vocab_size=50, d_model=32, nhead=2, num_layers=1, num_classes=3)
    x = torch.randint(0, 50, (2, 10))
    out = model(x)
    assert out is not None
    assert not torch.isnan(out).any()

import pytest
import torch
from src.dl.transformer import TransformerClassifier


def test_transformer_output_shape():
    model = TransformerClassifier(vocab_size=100, d_model=64, nhead=4, num_layers=2, num_classes=2)
    x = torch.randint(0, 100, (4, 20))
    out = model(x)
    assert out.shape == (4, 2)

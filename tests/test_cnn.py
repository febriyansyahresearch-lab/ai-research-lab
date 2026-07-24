import pytest
import torch
from src.models.cnn import CNN1D, CNN2D


def test_cnn1d_output_shape():
    model = CNN1D(input_dim=8, num_classes=2, hidden_dim=32)
    x = torch.randn(4, 10, 8)
    out = model(x)
    assert out.shape == (4, 2)


def test_cnn2d_output_shape():
    model = CNN2D(num_classes=10)
    x = torch.randn(4, 1, 28, 28)
    out = model(x)
    assert out.shape == (4, 10)


def test_cnn1d_forward_pass():
    model = CNN1D(input_dim=4, num_classes=3, hidden_dim=16)
    x = torch.randn(2, 5, 4)
    out = model(x)
    assert out is not None
    assert not torch.isnan(out).any()

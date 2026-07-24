import pytest
import torch
from intrusion_dl.src.model import IntrusionLSTM


def test_model_output_shape():
    model = IntrusionLSTM(n_features=8, hidden_dim=32, num_classes=2)
    x = torch.randn(4, 20, 8)
    out = model(x)
    assert out.shape == (4, 2)

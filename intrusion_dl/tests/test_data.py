import pytest
from intrusion_dl.src.data import generate_network_flows, FlowDataset


def test_generate_flows_shape():
    X, y = generate_network_flows(100, 50, seq_length=10, n_features=4)
    assert X.shape == (150, 10, 4)
    assert y.shape == (150,)
    assert set(y.tolist()) == {0, 1}


def test_flow_dataset():
    import numpy as np
    X = np.random.randn(10, 5, 3).astype(np.float32)
    y = np.zeros(10, dtype=np.int64)
    ds = FlowDataset(X, y)
    assert len(ds) == 10
    x, lbl = ds[0]
    assert x.shape == (5, 3)

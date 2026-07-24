import pytest
from src.utils.data_loader import create_sequence_data, generate_synthetic_logs, get_dataloader


def test_create_sequence_data_shape():
    X, y = create_sequence_data(n_samples=100, seq_length=10, n_features=8)
    assert X.shape == (100, 10, 8)
    assert y.shape == (100,)


def test_generate_synthetic_logs_shape():
    X, y = generate_synthetic_logs(n_samples=100, seq_length=20)
    assert X.shape == (100, 20, 4)
    assert y.shape == (100,)


def test_get_dataloader():
    X, y = create_sequence_data(n_samples=32, seq_length=5, n_features=4)
    loader = get_dataloader(X, y, batch_size=8)
    batch = next(iter(loader))
    assert batch[0].shape == (8, 5, 4)

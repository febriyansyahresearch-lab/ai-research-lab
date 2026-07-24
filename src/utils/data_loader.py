import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


class SequenceDataset(Dataset):
    def __init__(self, sequences, labels):
        self.sequences = torch.tensor(sequences, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.sequences[idx], self.labels[idx]


def create_sequence_data(n_samples: int = 1000, seq_length: int = 10, n_features: int = 8, random_state: int = 42):
    np.random.seed(random_state)
    X = np.random.randn(n_samples, seq_length, n_features).astype(np.float32)
    y = (X[:, -1, 0] > 0).astype(np.int64)
    return X, y


def generate_synthetic_logs(n_samples: int = 500, seq_length: int = 20):
    np.random.seed(42)
    normal = np.random.randn(n_samples // 2, seq_length, 4) * 0.5
    anomaly = np.random.randn(n_samples // 2, seq_length, 4) * 2.0 + 1.0
    X = np.vstack([normal, anomaly]).astype(np.float32)
    y = np.hstack([np.zeros(n_samples // 2), np.ones(n_samples // 2)]).astype(np.int64)
    return X, y


def get_dataloader(X, y, batch_size: int = 32, shuffle: bool = True):
    dataset = SequenceDataset(X, y)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

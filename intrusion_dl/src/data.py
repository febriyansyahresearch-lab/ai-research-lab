import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


def generate_network_flows(n_normal: int = 500, n_attack: int = 200, seq_length: int = 20, n_features: int = 8) -> tuple[np.ndarray, np.ndarray]:
    np.random.seed(42)

    normal = np.random.randn(n_normal, seq_length, n_features) * 0.3
    attack = np.random.randn(n_attack, seq_length, n_features) * 0.8 + 0.5

    X = np.vstack([normal, attack]).astype(np.float32)
    y = np.hstack([np.zeros(n_normal), np.ones(n_attack)]).astype(np.int64)

    shuffle = np.random.permutation(len(y))
    return X[shuffle], y[shuffle]


class FlowDataset(Dataset):
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


def get_loaders(batch_size: int = 32) -> tuple[DataLoader, DataLoader]:
    X, y = generate_network_flows()
    split = int(len(y) * 0.8)
    train_ds = FlowDataset(X[:split], y[:split])
    test_ds = FlowDataset(X[split:], y[split:])
    return DataLoader(train_ds, batch_size=batch_size, shuffle=True), DataLoader(test_ds, batch_size=batch_size)

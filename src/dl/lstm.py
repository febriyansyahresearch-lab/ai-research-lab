import torch
import torch.nn as nn


class LSTMClassifier(nn.Module):
    """LSTM untuk klasifikasi sequence (log, time series)."""

    def __init__(self, input_dim: int, hidden_dim: int = 128, num_layers: int = 2, num_classes: int = 2, dropout: float = 0.3):
        super().__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True, dropout=dropout)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = out[:, -1, :]
        return self.fc(out)


class BiLSTMClassifier(nn.Module):
    """Bidirectional LSTM untuk konteks dua arah."""

    def __init__(self, input_dim: int, hidden_dim: int = 128, num_layers: int = 2, num_classes: int = 2, dropout: float = 0.3):
        super().__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True, bidirectional=True, dropout=dropout)
        self.fc = nn.Linear(hidden_dim * 2, num_classes)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = out[:, -1, :]
        return self.fc(out)

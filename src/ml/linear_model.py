import numpy as np


class LinearRegression:
    def __init__(self, lr: float = 0.01, epochs: int = 1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.epochs):
            preds = X @ self.weights + self.bias
            dw = (2 / n_samples) * X.T @ (preds - y)
            db = (2 / n_samples) * np.sum(preds - y)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X: np.ndarray) -> np.ndarray:
        return X @ self.weights + self.bias


class LogisticRegression:
    def __init__(self, lr: float = 0.01, epochs: int = 1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.epochs):
            preds = self._sigmoid(X @ self.weights + self.bias)
            dw = (1 / n_samples) * X.T @ (preds - y)
            db = (1 / n_samples) * np.sum(preds - y)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X: np.ndarray) -> np.ndarray:
        return (self._sigmoid(X @ self.weights + self.bias) >= 0.5).astype(int)

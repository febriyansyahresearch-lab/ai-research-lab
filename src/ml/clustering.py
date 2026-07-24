import numpy as np


class KMeans:
    def __init__(self, n_clusters: int = 3, max_iter: int = 100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit(self, X: np.ndarray):
        idx = np.random.choice(len(X), self.n_clusters, replace=False)
        self.centroids = X[idx]
        for _ in range(self.max_iter):
            labels = self.predict(X)
            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids

    def predict(self, X: np.ndarray) -> np.ndarray:
        dists = np.linalg.norm(X[:, None] - self.centroids[None], axis=2)
        return np.argmin(dists, axis=1)

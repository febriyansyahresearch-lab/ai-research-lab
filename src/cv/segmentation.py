import numpy as np


class SimpleSegmenter:
    def __init__(self, n_clusters: int = 3):
        self.n_clusters = n_clusters

    def kmeans_segment(self, image: np.ndarray) -> np.ndarray:
        pixels = image.reshape(-1, 3)
        centroids = pixels[np.random.choice(len(pixels), self.n_clusters, replace=False)]
        for _ in range(20):
            dists = np.linalg.norm(pixels[:, None] - centroids[None], axis=2)
            labels = np.argmin(dists, axis=1)
            new_centroids = np.array([pixels[labels == k].mean(axis=0) for k in range(self.n_clusters)])
            if np.allclose(centroids, new_centroids):
                break
            centroids = new_centroids
        segmented = centroids[labels].reshape(image.shape).astype(np.uint8)
        return segmented

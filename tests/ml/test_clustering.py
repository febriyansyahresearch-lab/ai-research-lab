import pytest
import numpy as np
from src.ml.clustering import KMeans


def test_kmeans():
    X = np.array([[1, 1], [1, 2], [2, 1], [10, 10], [10, 11], [11, 10]])
    model = KMeans(n_clusters=2, max_iter=50)
    model.fit(X)
    labels = model.predict(X)
    assert len(set(labels)) == 2
    assert labels[0] == labels[2]
    assert labels[3] == labels[5]

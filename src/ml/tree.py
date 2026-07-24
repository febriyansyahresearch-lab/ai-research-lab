import numpy as np
from collections import Counter


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value


class DecisionTree:
    def __init__(self, max_depth: int = 5):
        self.max_depth = max_depth
        self.root = None

    def _gini(self, y: np.ndarray) -> float:
        probs = np.bincount(y) / len(y)
        return 1 - np.sum(probs ** 2)

    def _split(self, X: np.ndarray, y: np.ndarray, feature: int, threshold: float):
        left = y[X[:, feature] <= threshold]
        right = y[X[:, feature] > threshold]
        return left, right

    def _best_split(self, X: np.ndarray, y: np.ndarray):
        best_gini = float("inf")
        best_feat, best_thresh = None, None
        for feat in range(X.shape[1]):
            thresholds = np.unique(X[:, feat])
            for thresh in thresholds:
                left, right = self._split(X, y, feat, thresh)
                if len(left) == 0 or len(right) == 0:
                    continue
                gini = (len(left) * self._gini(left) + len(right) * self._gini(right)) / len(y)
                if gini < best_gini:
                    best_gini = gini
                    best_feat = feat
                    best_thresh = thresh
        return best_feat, best_thresh

    def _build(self, X: np.ndarray, y: np.ndarray, depth: int) -> Node:
        if depth >= self.max_depth or len(np.unique(y)) == 1:
            return Node(value=Counter(y).most_common(1)[0][0])

        feat, thresh = self._best_split(X, y)
        if feat is None:
            return Node(value=Counter(y).most_common(1)[0][0])

        left_idx = X[:, feat] <= thresh
        right_idx = X[:, feat] > thresh
        left = self._build(X[left_idx], y[left_idx], depth + 1)
        right = self._build(X[right_idx], y[right_idx], depth + 1)
        return Node(feature=feat, threshold=thresh, left=left, right=right)

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.root = self._build(X, y, 0)

    def _traverse(self, x: np.ndarray, node: Node) -> int:
        if node.value is not None:
            return node.value
        if x[node.feature] <= node.threshold:
            return self._traverse(x, node.left)
        return self._traverse(x, node.right)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.array([self._traverse(x, self.root) for x in X])

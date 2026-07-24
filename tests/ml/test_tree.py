import pytest
import numpy as np
from src.ml.tree import DecisionTree


def test_decision_tree():
    X = np.array([[1], [2], [3], [4], [5], [6]])
    y = np.array([0, 0, 0, 1, 1, 1])
    tree = DecisionTree(max_depth=3)
    tree.fit(X, y)
    preds = tree.predict(X)
    assert np.array_equal(preds, y)

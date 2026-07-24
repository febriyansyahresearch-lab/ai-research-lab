import pytest
import numpy as np
from src.ml.linear_model import LinearRegression, LogisticRegression


def test_linear_regression_fit():
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8])
    model = LinearRegression(lr=0.01, epochs=500)
    model.fit(X, y)
    preds = model.predict(X)
    assert np.allclose(preds, y, atol=1.0)


def test_logistic_regression_fit():
    X = np.array([[1], [2], [3], [4], [5], [6]])
    y = np.array([0, 0, 0, 1, 1, 1])
    model = LogisticRegression(lr=0.1, epochs=500)
    model.fit(X, y)
    preds = model.predict(X)
    assert np.array_equal(preds, y)

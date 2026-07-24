import pytest
import numpy as np
from src.autonomous.path_planning import a_star_grid, dijkstra_grid


def test_a_star_finds_path():
    grid = np.zeros((5, 5), dtype=int)
    path = a_star_grid(grid, (0, 0), (4, 4))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (4, 4)


def test_a_star_returns_none():
    grid = np.ones((5, 5), dtype=int)
    path = a_star_grid(grid, (0, 0), (4, 4))
    assert path is None


def test_dijkstra():
    grid = np.zeros((3, 3), dtype=int)
    distances = dijkstra_grid(grid, (0, 0))
    assert (0, 0) in distances

import pytest
from src.core.search import bfs, dfs


def test_bfs_finds_path():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    path = bfs(graph, "A", "D")
    assert path is not None
    assert path[0] == "A"
    assert path[-1] == "D"


def test_bfs_no_path():
    graph = {"A": ["B"], "B": [], "C": []}
    path = bfs(graph, "A", "C")
    assert path is None


def test_dfs_finds_path():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    path = dfs(graph, "A", "D")
    assert path is not None
    assert path[-1] == "D"

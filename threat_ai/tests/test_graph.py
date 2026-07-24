import pytest
from threat_ai.src.graph import AttackGraph


def test_attack_path():
    g = AttackGraph()
    for n in ["A", "B", "C", "D"]:
        g.add_node(n, risk=0.5)
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")

    path = g.find_attack_path("A", "D")
    assert path == ["A", "B", "C", "D"]


def test_no_path():
    g = AttackGraph()
    g.add_node("A")
    g.add_node("B")
    path = g.find_attack_path("A", "B")
    assert path is None

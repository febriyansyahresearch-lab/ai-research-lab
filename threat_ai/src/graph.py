from collections import deque
import heapq


class AttackGraph:
    def __init__(self):
        self.nodes: dict[str, dict] = {}
        self.edges: dict[str, list[tuple[str, float]]] = {}

    def add_node(self, node_id: str, label: str = "", risk: float = 0.0):
        self.nodes[node_id] = {"label": label, "risk": risk}
        if node_id not in self.edges:
            self.edges[node_id] = []

    def add_edge(self, src: str, dst: str, cost: float = 1.0):
        if src not in self.edges:
            self.edges[src] = []
        self.edges[src].append((dst, cost))

    def find_attack_path(self, start: str, goal: str) -> list[str] | None:
        queue = deque([[start]])
        visited = {start}
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == goal:
                return path
            for neighbor, _ in self.edges.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def highest_risk_path(self, start: str, goal: str) -> list[str] | None:
        pq = [(-self.nodes.get(start, {}).get("risk", 0), start, [start])]
        visited = {}
        while pq:
            neg_risk, node, path = heapq.heappop(pq)
            if node == goal:
                return path
            if node in visited and visited[node] >= -neg_risk:
                continue
            visited[node] = -neg_risk
            for neighbor, _ in self.edges.get(node, []):
                risk = -neg_risk + self.nodes.get(neighbor, {}).get("risk", 0)
                heapq.heappush(pq, (-risk, neighbor, path + [neighbor]))
        return None

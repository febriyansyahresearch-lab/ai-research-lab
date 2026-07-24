from collections import deque
import heapq
from typing import Callable


def bfs(graph: dict, start: str, goal: str) -> list[str] | None:
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


def dfs(graph: dict, start: str, goal: str, path: list[str] | None = None, visited: set | None = None) -> list[str] | None:
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result
    return None


def a_star(graph: dict, start: str, goal: str, heuristic: Callable[[str, str], float]) -> list[str] | None:
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.get(current, {}).items():
            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score[neighbor] = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

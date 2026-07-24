import heapq
import numpy as np


def _neighbors(grid: np.ndarray, pos: tuple[int, int]):
    h, w = grid.shape
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = pos[0] + dy, pos[1] + dx
        if 0 <= ny < h and 0 <= nx < w and grid[ny, nx] == 0:
            yield ny, nx


def a_star_grid(grid: np.ndarray, start: tuple[int, int], goal: tuple[int, int]) -> list[tuple[int, int]] | None:
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

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

        for neighbor in _neighbors(grid, current):
            tentative = g_score[current] + 1
            if tentative < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score[neighbor] = tentative + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None


def dijkstra_grid(grid: np.ndarray, start: tuple[int, int]) -> dict:
    distances = {start: 0}
    pq = [(0, start)]
    while pq:
        dist, current = heapq.heappop(pq)
        if dist > distances.get(current, float("inf")):
            continue
        for neighbor in _neighbors(grid, current):
            nd = dist + 1
            if nd < distances.get(neighbor, float("inf")):
                distances[neighbor] = nd
                heapq.heappush(pq, (nd, neighbor))
    return distances

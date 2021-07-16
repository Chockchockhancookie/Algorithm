from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline


def bfs(x, y, visited):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if edges[nx][ny] == 0:
                    edges[nx][ny] = 2
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def count_empty(edges):
    count = 0
    for i in range(n):
        for j in range(m):
            if edges[i][j] == 0:
                count += 1
    return count


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

virus = []
for a in range(n):
    for b in range(m):
        if graph[a][b] == 0:
            virus.append((a, b))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
for ch in combinations(virus, 3):
    edges = deepcopy(graph)
    visited = [[False] * m for _ in range(n)]

    for x, y in ch:
        edges[x][y] = 1

    for a in range(n):
        for b in range(m):
            if edges[a][b] == 2 and not visited[a][b]:
                bfs(a, b, visited)

    answer = max(answer, count_empty(edges))

print(answer)
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while queue:
        x, y, w = queue.popleft()
        print(x, y)
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] =   visited[x][y][1] + 1
                    queue.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
    return -1


n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = int(1e9)
print(bfs())
from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and visited[nz][nx][ny] == 0 and graph[nz][nx][ny] == 0:
                queue.append((nx, ny, nz))
                visited[nz][nx][ny] = 1
                graph[nz][nx][ny] = graph[z][x][y] + 1


m, n, h = map(int, input().split())

graph = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)

visited = [[[0] * m for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1:
                queue.append([b, c, a])

bfs()

answer = 0
for floor in graph:
    for data in floor:
        if 0 in data:
            print(-1)
            sys.exit(0)
        answer = max(answer, max(data))

print(answer-1)
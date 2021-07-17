from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, land):
    graph[x][y] = land
    queue = deque()
    queue.append((x, y, land))
    while queue:
        x, y, land = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if edges[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = land
                    queue.append((nx, ny, land))


def bfs2(num):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if edges[nx][ny] == 1 and graph[nx][ny] != num:
                    return data[x][y] - 1
                if edges[nx][ny] == 0 and data[nx][ny] == 0:
                    data[nx][ny] = data[x][y] + 1
                    q.append([nx, ny])


n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
land = 1
for a in range(n):
    for b in range(n):
        if edges[a][b] == 1 and not visited[a][b]:
            visited[a][b] = True
            bfs(a, b, land)
            land += 1

answer = int(1e9)
for i in range(1, land):
    q = deque()
    data = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if edges[a][b] == 1 and graph[a][b] == i:
                q.append((a, b))
                data[a][b] = 1

    final = bfs2(i)
    answer = min(answer, final)

print(answer)
from collections import deque


def bfs(x, y):
    visited[x][y] = True
    tmp_visited = [[False] * (m+1) for _ in range(n+1)]
    tmp_visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < n+1 and 0 < ny < m+1:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    tmp_visited[nx][ny] = True
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    num = 0
    for a in range(1, n+1):
        for b in range(1, m+1):
            if tmp_visited[a][b]:
                num += 1
    return num


n, m, k = map(int, input().split())
graph = [[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

visited = [[False] * (m+1) for _ in range(n+1)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0
for a in range(1, n+1):
    for b in range(1, m+1):
        if graph[a][b] == 1 and not visited[a][b]:
            count = bfs(a, b)
            result = max(result, count)

print(result)

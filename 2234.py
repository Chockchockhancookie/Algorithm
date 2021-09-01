from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, now):
    visited[x][y] = now
    queue = deque()
    queue.append((x, y))
    dist = 1
    while queue:
        x, y = queue.popleft()
        tmp = graph[x][y]
        for i in range(len(dx[tmp])):
            nx = x + dx[tmp][i]
            ny = y + dy[tmp][i]
            if visited[nx][ny] == -1:
                dist += 1
                visited[nx][ny] = now
                queue.append((nx, ny))
    sum_value[now] = dist
    return dist


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [[], [1, 0, -1], [1, 0, 0], [1, 0], [1, -1, 0], [1, -1], [1, 0],
      [1], [0, -1, 0], [0, -1], [0, 0], [0], [-1, 0], [-1], [0], []]
dy = [[], [0, 1, 0], [0, 1, -1], [0, 1], [0, 0, -1], [0, 0], [0, -1],
      [0], [1, 0, -1], [1, 0], [1, -1], [1], [0, -1], [0], [-1], []]

visited = [[-1] * m for _ in range(n)]
sum_value = {}
count = 0
max_dist = 0
for a in range(n):
    for b in range(m):
        if visited[a][b] == -1:
            count += 1
            max_dist = max(max_dist, bfs(a, b, count))

print(count)
print(max_dist)

da = [1, 0, -1, 0]
db = [0, -1, 0, 1]

check = 0
for a in range(n):
    for b in range(m):
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if 0 <= na < n and 0 <= nb < m and visited[a][b] != visited[na][nb]:
                check = max(check, sum_value[visited[a][b]]+sum_value[visited[na][nb]])

print(check)
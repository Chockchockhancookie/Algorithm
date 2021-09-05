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
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                print(i, arr[i], graph[nx][ny], ~graph[nx][ny], arr[i] & ~graph[nx][ny])
                if arr[i] & ~graph[nx][ny] and visited[nx][ny] == -1:
                    dist += 1
                    visited[nx][ny] = now
                    queue.append((nx, ny))
    sum_data[now] = dist
    return dist


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

arr = [1, 2, 4, 8]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[-1] * m for _ in range(n)]

count = 0
max_dist = 0
sum_data = {}
for a in range(n):
    for b in range(m):
        if visited[a][b] == -1:
            count += 1
            max_dist = max(max_dist, bfs(a, b, count))

print(count)
print(max_dist)

check = 0
for a in range(n):
    for b in range(m):
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < n and 0 <= nb < m and visited[a][b] != visited[na][nb]:
                check = max(check, sum_data[visited[a][b]] + sum_data[visited[na][nb]])

print(check)
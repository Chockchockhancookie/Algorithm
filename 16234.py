from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, idx):
    arr = []
    arr.append([x, y])
    queue = deque()
    queue.append((x, y))
    visited[x][y] = idx
    count = 1
    sum_value = graph[x][y]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and l <= abs(graph[x][y]-graph[nx][ny]) <= r and visited[nx][ny] == -1:
                visited[nx][ny] = idx
                sum_value += graph[nx][ny]
                count += 1
                queue.append((nx, ny))
                arr.append([nx, ny])

    tmp = sum_value//count
    for i, j in arr:
        graph[i][j] = tmp


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
while True:
    visited = [[-1] * n for _ in range(n)]
    idx = 0
    for a in range(n):
        for b in range(n):
            if visited[a][b] == -1:
                bfs(a, b, idx)
                idx += 1

    if idx == n*n:
        break

    answer += 1

print(answer)
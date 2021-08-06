from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


t = int(input())

answers = []
for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * m for _ in range(n)]

    answer = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                if not visited[a][b]:
                    bfs(a, b)
                    answer += 1

    answers.append(answer)

for answer in answers:
    print(answer)
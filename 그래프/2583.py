from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
    return count


n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    left_y, left_x, right_y, right_x = map(int, input().split())
    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            graph[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]

answers = []
cnt = 0
for a in range(n):
    for b in range(m):
        if not visited[a][b] and graph[a][b] == 0:
            cnt += 1
            visited[a][b] = True
            answers.append(bfs(a, b))

print(cnt)
answers.sort()
for answer in answers:
    print(answer, end=" ")
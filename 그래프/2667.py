from collections import deque


def bfs(x, y, count):
    visited[x][y] = count
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = count
                    queue.append((nx, ny))
    num = 0
    for a in range(n):
        for b in range(n):
            if visited[a][b] == count:
                num += 1
    return num


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = []
count = 0
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1 and visited[a][b] == 0:
            count += 1
            result = bfs(a, b, count)
            answer.append(result)

answer.sort()
print(count)
for i in answer:
    print(i)

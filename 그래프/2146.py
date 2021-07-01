from collections import deque


def make_land(x, y, land):
    lands[x][y] = land
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and lands[nx][ny] == 0:
                    lands[nx][ny] = land
                    queue.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

lands = [[0] * n for _ in range(n)]
land = 1
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1 and not lands[a][b]:
            make_land(a, b, land)
            land += 1

for
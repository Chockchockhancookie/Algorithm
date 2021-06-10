def move_water(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= 0:
            continue
        if graph[nx][ny] == "D" or graph[nx][ny] == "X":
            continue
        graph[nx][ny] = "*"


n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    for a in range(n):
        for b in range(m):
            if graph[a][b] == "*":
                move_water(a, b)
            
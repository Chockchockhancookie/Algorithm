from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    graph[a][b] = 0
    queue = deque()
    queue.append((a, b))
    while queue or water:
        tmp_queue = []
        tmp_water = []
        while queue:
            x, y = queue.popleft()
            if graph[x][y] != "*":
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                        if graph[nx][ny] == "." or graph[nx][ny] == "D":
                            graph[nx][ny] = graph[x][y] + 1
                            visited[nx][ny] = True
                            tmp_queue.append((nx, ny))

        while water:
            i, j = water.popleft()
            for a in range(4):
                ni = i + dx[a]
                nj = j + dy[a]
                if ni == end_x and nj == end_y:
                    continue
                if 0 <= ni < r and 0 <= nj < c and graph[ni][nj] != "*" and graph[ni][nj] != "X":
                    graph[ni][nj] = "*"
                    tmp_water.append((ni, nj))

        for tmp in tmp_queue:
            queue.append(tmp)

        for tmp in tmp_water:
            water.append(tmp)


r, c = map(int, input().split())
graph = []
water = deque()

visited = [[False] * c for _ in range(r)]

start_x, start_y = 0, 0
end_x, end_y = 0, 0
for i in range(r):
    tmp = list(input().rstrip())
    graph.append(tmp)
    for j in range(c):
        if tmp[j] == "S":
            start_x, start_y = i, j
            visited[i][j] = True
        elif tmp[j] == "*":
            water.append((i, j))
        elif tmp[j] == "D":
            end_x, end_y = i, j

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

bfs(start_x, start_y)
if graph[end_x][end_y] == "D":
    print("KAKTUS")
else:
    print(graph[end_x][end_y])
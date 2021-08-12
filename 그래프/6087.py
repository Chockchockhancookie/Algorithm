from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)


def bfs(x, y):
    distance = [[INF] * m for _ in range(n)]
    distance[x][y] = 0
    queue = deque()
    queue.append((x, y, 9, 0))
    while queue:
        a, b, direct, count = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "*":
                if i != direct:
                    if direct == 9:
                        cost = count
                        if cost <= distance[nx][ny]:
                            distance[nx][ny] = cost
                            queue.append((nx, ny, i, cost))
                    cost = count + 1
                    if cost <= distance[nx][ny]:
                        distance[nx][ny] = cost
                        queue.append((nx, ny, i, cost))
                else:
                    cost = count
                    if cost <= distance[nx][ny]:
                        distance[nx][ny] = cost
                        queue.append((nx, ny, i, cost))
    return distance


m, n = map(int, input().split())
start_x, start_y = -1, -1
end_x, end_y = -1, -1

graph = []
for i in range(n):
    tmp = list(input().rstrip())
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == "C":
            if start_x == -1:
                start_x, start_y = i, j
            else:
                end_x, end_y = i, j

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = bfs(start_x, start_y)

if answer[end_x][end_y] == INF:
    print(0)
else:
    print(answer[end_x][end_y])
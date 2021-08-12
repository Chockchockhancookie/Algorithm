from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)


def escape_room(x, y):
    array = [[INF] * m for _ in range(n)]
    array[x][y] = 0
    queue = deque()
    queue.append((x, y, 0))
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == ".":
                cost = dist + 1
                if cost < array[nx][ny]:
                    array[nx][ny] = cost
                    queue.append((nx, ny, cost))
    return array


def spread_fire():
    data = [[INF] * m for _ in range(n)]
    queue = deque()
    for i, j in fires:
        queue.append((i, j, 0))
        data[i][j] = 0

    while queue:
        a, b, dist = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == ".":
                cost = dist + 1
                if cost < data[nx][ny]:
                    data[nx][ny] = cost
                    queue.append((nx, ny, cost))

    return data


n, m = map(int, input().split())
x, y = 0, 0
fires = []

graph = []
for i in range(n):
    tmp = list(input().rstrip())
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == "J":
            x, y = i, j
        elif tmp[j] == "F":
            fires.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

jihoon = escape_room(x, y)
fire = spread_fire()

answer = INF
for a in range(n):
    for b in range(m):
        if a == 0 or a == n-1 or b == 0 or b == m-1:
            if jihoon[a][b] < fire[a][b]:
                answer = min(answer, jihoon[a][b])

if answer < INF:
    print(answer+1)
else:
    print("IMPOSSIBLE")
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)


# 모든 위치의 최단 거리
def bfs():
    distance = [[-1] * n for _ in range(n)]
    distance[start_x][start_y] = 0
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] == -1 and graph[nx][ny] <= baby_size:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    return distance


def find(distance):
    x, y = 0, 0
    min_value = INF
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 1 <= graph[i][j] < baby_size:
                if distance[i][j] < min_value:
                    x, y = i, j
                    min_value = distance[i][j]

    if min_value == INF:
        return None
    else:
        return x, y, min_value


n = int(input())
graph = []

start_x, start_y = 0, 0
baby_size = 2
for a in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for b in range(n):
        if tmp[b] == 9:
            start_x, start_y = a, b
            graph[start_x][start_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
eat = 0
while True:
    value = find(bfs())
    if value is None:
        print(answer)
        break
    else:
        start_x, start_y = value[0], value[1]
        answer += value[2]
        graph[start_x][start_y] = 0
        eat += 1
        if eat >= baby_size:
            baby_size += 1
            eat = 0
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(x, y):
    distance = [[INF] * n for _ in range(n)]
    distance[x][y] = graph[x][y]
    queue = []
    heapq.heappush(queue, (graph[x][y], x, y))
    while queue:
        dist, x, y = heapq.heappop(queue)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost =  dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, nx, ny))
    return distance


answer = []
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    result = dijkstra(0, 0)
    answer.append(result[n-1][n-1])

for i in range(len(answer)):
    print("Problem {}: {}".format(i+1, answer[i]))
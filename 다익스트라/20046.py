import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(x, y):
    distance = [[INF] * m for _ in range(n)]
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
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != -1:
                    cost = dist + graph[nx][ny]
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(queue, (cost, nx, ny))

    return distance[n-1][m-1]


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

if graph[0][0] == -1:
    print(-1)
    sys.exit()
else:
    answer = dijkstra(0, 0)

if answer >= INF:
    print(-1)
else:
    print(answer)
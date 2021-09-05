import heapq
import sys
input = sys.stdin.readline


def dijkstra(x, y):
    distance = [[-1] * n for _ in range(n)]
    queue = []
    heapq.heappush(queue, (0, x, y))
    while queue:
        dist, x, y = heapq.heappop(queue)

        if distance[x][y] != -1:
            continue

        if x == n-1 and y == n-1:
            return dist

        distance[x][y] = dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] == -1:
                    tmp = max(dist, abs(graph[x][y]-graph[nx][ny]))
                    heapq.heappush(queue, (tmp, nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(dijkstra(0, 0))
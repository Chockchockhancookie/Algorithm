import heapq
import sys
input = sys.stdin.readline


def dijkstra():
    queue = []
    visited[0][0] = True
    heapq.heappush(queue, (0, 0, 0))  # cost, x, y
    while queue:
        cost, x, y = heapq.heappop(queue)
        if x == n-1 and y == n-1:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    heapq.heappush(queue, (cost+1, nx, ny))
                elif not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    heapq.heappush(queue, (cost, nx, ny))


n = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

print(dijkstra())
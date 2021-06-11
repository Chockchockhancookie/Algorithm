from collections import deque
import heapq
INF = int(1e9)


def dijkstra(start, end):
    visited = [INF] * (n+1)
    visited[a] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, now = heapq.heappop(queue)
        if now == end:
            continue
        if visited[now] < cost:
            continue
        cost += 1
        for i in alpha[now]:
            if cost < visited[i]:
                visited[i] = cost
                heapq.heappush(queue, (cost, i))
    return visited[end]


a, b = map(int, input().split())

n, m = map(int, input().split())

alpha = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    alpha[x].append(y)
    alpha[y].append(x)

answer = dijkstra(a, b)
if answer == INF:
    print(-1)
else:
    print(answer)
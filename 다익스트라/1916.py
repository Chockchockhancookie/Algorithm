import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in edges[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance[end]


n = int(input())
m = int(input())

edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])

start, end = map(int, input().split())

print(dijkstra(start))
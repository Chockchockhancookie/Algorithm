import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance


n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])
    graph[b].append([a, 1])

answer = [0] * (n+1)
for i in range(1, n+1):
    distance = dijkstra(i)
    answer[i] = sum(distance[1:])

final = answer[1:]
print(final.index(min(final))+1)
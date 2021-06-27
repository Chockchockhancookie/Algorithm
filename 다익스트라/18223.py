import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (v + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for n, c in graph[now]:
            cost = dist + c
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(queue, (cost, n))
    return distance


v, e, p = map(int, input().split())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

array = dijkstra(1)
arr = dijkstra(p)
tmp1 = array[v]
tmp2 = array[p] + arr[v]

if tmp1 == tmp2:
    print("SAVE HIM")
else:
    print("GOOD BYE")


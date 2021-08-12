import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in edges[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(queue, (cost, i))
    return distance[end]


n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, n+1):
        if tmp[j-1]:
            edges[i].append(j)

plans = list(map(int, input().split()))

check = True
for i in range(len(plans)-1):
    start, end = plans[i], plans[i+1]
    tmp = dijkstra(start, end)
    if tmp == INF:
        check = False
        break

if check:
    print("YES")
else:
    print("NO")

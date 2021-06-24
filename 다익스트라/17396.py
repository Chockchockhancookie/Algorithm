import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v] and edge[v] == 0:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [INF] * n
edge = list(map(int, input().split()))
edge[-1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

dijkstra(0)
if distance[n-1] != INF:
    print(distance[n-1])
else:
    print(-1)


# import heapq
# import sys
# INF = sys.maxsize
# input = sys.stdin.readline
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     dis[start] = 0
#     while q:
#         d, now = heapq.heappop(q)
#         if dis[now] < d:
#             continue
#         for v, w in graph[now]:
#             cost = d + w
#             if cost < dis[v] and check[v] == 0:
#                 dis[v] = cost
#                 heapq.heappush(q, (cost, v))
#
# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# dis = [INF]*(N+1)
# check = list(map(int, input().split()))
# check[-1] = 0
# for _ in range(M):
#     a, b, t = map(int, input().split())
#     graph[a].append((b, t))
#     graph[b].append((a, t))
# dijkstra(0)
# print(dis[N-1] if dis[N-1] != INF else -1)
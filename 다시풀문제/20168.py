import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    global answer
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, 0, start))
    while queue:
        d, dist, now = heapq.heappop(queue)

        if money < dist:
            continue
        else:
            if now == end:
                answer = min(answer, d)

        for i in edges[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (max(d, i[1]), cost, i[0]))

    return distance


n, m, start, end, money = map(int, input().split())

edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

answer = INF
dijkstra(start)

if answer == INF:
    print(-1)
else:
    print(answer)
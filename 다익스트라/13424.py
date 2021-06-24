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
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    count = 0
    for a in room:
        count += distance[a]
    return count


t = int(input())
answer = []
for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    k = int(input())
    room = list(map(int, input().split()))

    check = INF
    final = INF
    for i in range(1, n+1):
        tmp = dijkstra(i)
        if tmp < final:
            final = tmp
            check = i

    answer.append(check)

for i in answer:
    print(i)
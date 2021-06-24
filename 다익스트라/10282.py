import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline


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
    return distance


t = int(input())
answer = []
for _ in range(t):
    n, d, c = map(int, input().split())    # 컴퓨터의 수, 의존성 개수, 해킹당한 컴퓨터의 번호

    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, second = map(int, input().split())
        graph[b].append((a, second))

    count = 0
    num = 0
    result = dijkstra(c)
    for i in range(1, n+1):
        if result[i] != INF:
            count += 1
            num = max(num, result[i])

    answer.append((count, num))

for i in answer:
    print(i[0], i[1])
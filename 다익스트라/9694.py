import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * m
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    while queue:
        dist, now, array = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        if now == m-1:
            return array

        for i in edges[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0], array+[i[0]]))
    return


t = int(input())
answers = [[]]
for i in range(1, t+1):
    n, m = map(int, input().split())

    edges = [[] for _ in range(m)]
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges[x].append([y, z])
        edges[y].append([x, z])

    tmp = dijkstra(0)
    if tmp is None:
        answers.append([-1])
    else:
        answers.append(tmp)

for i in range(1, t+1):
    print("Case #{}:".format(i), end=" ")
    for j in range(len(answers[i])):
        print(answers[i][j], end=" ")
    print()

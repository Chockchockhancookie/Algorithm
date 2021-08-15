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
        for i in edges[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


n, m, x, y = map(int, input().split())  # 집의 수, 도로의 수, 최대 거리, 성현이 집

edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

distance = [INF] * n
dijkstra(y)

distance.sort()     # 가까운 집부터 방문해야함으로 정렬한다.
count = 0
answer = 0
for dist in distance:
    tmp = 2 * dist
    if tmp > x:
        print(-1)
        sys.exit(0)
    else:
        if count+tmp > x:
            answer += 1
            count = tmp
        else:
            count += tmp

print(answer+1)
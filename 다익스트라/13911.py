import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(distance, store, z):
    queue = []
    # 기존에 나는 집을 기준으로 항상 풀었지만 이번에는 가게를 기준으로 heap에 넣는다.
    for i in range(len(store)):
        heapq.heappush(queue, (0, store[i]))
        distance[store[i]]=0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in edges[now]:
            cost = dist + i[1]
            if cost <= z and cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]

mac_distance = [INF] * (v+1)
star_distance = [INF] * (v+1)
for i in range(e):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

m, x = map(int, input().split())
mac = list(map(int, input().split()))

dijkstra(mac_distance, mac, x)

s, y = map(int, input().split())
star = list(map(int, input().split()))

dijkstra(star_distance, star, y)

for i in range(1, v+1):
    if mac_distance[i] == 0 or star_distance[i] == 0:
        mac_distance[i] = INF
    else:
        mac_distance[i] += star_distance[i]

answer = min(mac_distance)

if answer >= INF:
    print(-1)
else:
    print(answer)
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)


def bfs(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = deque()
    queue.append((start, 0))
    while queue:
        now, dist = queue.popleft()
        if distance[now] < dist:
            continue
        for i in edges[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                queue.append((i[0], cost))
    return distance[end]


n, e = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

v1, v2 = map(int, input().split())

answer = min(bfs(1, v1) + bfs(v1, v2) + bfs(v2, n), bfs(1, v2) + bfs(v2, v1) + bfs(v1, n))

if answer >= INF:
    print(-1)
else:
    print(answer)
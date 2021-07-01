from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)


def bfs(start):
    distance[start] = 0
    queue = deque()
    queue.append([start, 0])
    while queue:
        now, dist = queue.popleft()
        for i in edges[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                queue.append([i, cost])
    return distance


n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

distance = [INF] * (n+1)

bfs(1)

node, dist, count = 0, 0, 0
for i in range(1, n+1):
    if distance[i] > dist:
        node = i
        dist = distance[i]
        count = 1
    elif distance[i] == dist:
        count += 1

print(node, dist, count)
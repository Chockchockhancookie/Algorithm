from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

distance = [0] * (n+1)

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        distance[i] = 1
        queue.append((i, 1))

while queue:
    now, dist = queue.popleft()
    if dist < distance[now]:
        continue
    for i in edges[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            cost = dist + 1
            if cost > distance[i]:
                distance[i] = cost
                queue.append((i, cost))

for i in range(1, n+1):
    print(distance[i], end = " ")
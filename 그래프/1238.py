from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)


def bfs(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = deque()
    queue.append((start, 0))
    while queue:
        now, dist = queue.popleft()
        if distance[now] < dist:
            continue
        for i in edges[now]:
            tmp = i[1] + dist
            if tmp < distance[i[0]]:
                distance[i[0]] = tmp
                queue.append((i[0], tmp))
    return distance


n, m, x = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges[a].append([b, cost])

answer = [INF] * (n+1)
answer[x] = 0
arr = None

for i in range(1, n+1):
    if i == x:
        arr = bfs(i)
    else:
        answer[i] = bfs(i)[x]

final = 0
for i in range(1, n+1):
    final = max(final, answer[i]+arr[i])

print(final)
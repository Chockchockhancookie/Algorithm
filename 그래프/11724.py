from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visited[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for node in edges[x]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (n+1)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)
from collections import deque
import sys
input = sys.stdin.readline

def dfs(node):
    print(node, end = ' ')
    visited[node] = True
    graph[node].sort()
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    queue = deque([node])
    visited[node] = False
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        graph[now].sort()
        for i in graph[now]:
            if visited[i]:
                queue.append(i)
                visited[i] = False


n, m, v = map(int, input().split())
graph = [[] * i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

dfs(v)
print()
bfs(v)

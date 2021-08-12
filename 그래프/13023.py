import sys
input = sys.stdin.readline


def dfs(start, count):
    global answer
    if count == 5:
        print(1)
        exit()
    for node in edges[start]:
        if not visited[node]:
            visited[node] = True
            dfs(node, count+1)
            visited[node] = False


n, m = map(int, input().split())
edges = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * n

answer = 0
for i in range(n):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(0)
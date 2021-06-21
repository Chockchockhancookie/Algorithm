def dfs(start, end):

    for i in edges[start]:
        if not visited[i]:
            visited[i] = True
            dfs(start, end)


n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges[a].append((b, cost))
    edges[b].append((a, cost))

start, end = map(int, input().split())

visited = [False] * (n+1)
visited[start] = True

answer = 0
dfs(start, end)

print()
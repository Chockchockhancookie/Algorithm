import sys
input = sys.stdin.readline


def dfs(start, cost):
    if cost == 4:
        print(1)
        exit()

    for i in edges[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cost+1)
            visited[i] = False


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
    dfs(i, 0)
    visited[i] = False

print(0)
import sys
input = sys.stdin.readline


def dfs(now, start):
    visited[now] = True
    

    for node in edges[now]:
        if not visited[node]:
            dfs(node, start)
        elif visited[node] and node == start:
            answer.append(start)


n = int(input())
edges = [[] for _ in range(n+1)]
for i in range(1, n+1):
    edges[i].append(int(input()))


answer = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)

print(len(answer))
for a in answer:
    print(a)
import sys
input = sys.stdin.readline


def dfs(node, dist, count):
    global answer
    if count == n-1:
        answer = min(answer, dist)
        return

    if dist > answer:
        return

    for a in range(n):
        if a != node and not visited[a]:
            visited[a] = True
            dfs(a, dist+graph[node][a], count+1)
            visited[a] = False


n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
visited[k] = True


for z in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][z] + graph[z][j])

answer = sys.maxsize
for i in range(n):
    if k != i and not visited[i]:
        visited[i] = True
        dfs(i, graph[k][i], 1)
        visited[i] = False

print(answer)
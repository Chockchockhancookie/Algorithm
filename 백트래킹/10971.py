import sys
input = sys.stdin.readline


def dfs(start, next, value, visited):
    global answer
    if len(visited) == n:
        if graph[next][start] != 0:
            answer = min(answer, value + graph[next][start])
        return
    for i in range(n):
        if i not in visited and graph[next][i] != 0 and start != i:
            visited.append(i)
            dfs(start, i, value + graph[next][i], visited)
            visited.pop()


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

answer = int(1e9)
for a in range(n):
    dfs(a, a, 0, [a])

print(answer)
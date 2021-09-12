import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 1:
        graph[u][v] = 1
        graph[v][u] = 1
    else:
        graph[u][v] = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        print(graph[a][b], end=" ")
    print()
print()

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] += 1

for a in range(1, n+1):
    for b in range(1, n+1):
        print(graph[a][b], end=" ")
    print()

k = int(input())

answer = []
for _ in range(k):
    s, e = map(int, input().split())
    answer.append(graph[s][e])

for a in answer:
    print(a)
import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())

edges = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

answer = sys.maxsize
for a in range(v):
    answer = min(answer, edges[a][a])

if answer == INF:
    print(-1)
else:
    print(answer)
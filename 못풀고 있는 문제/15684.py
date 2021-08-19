import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

graph = [[0] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(h+1):
    for b in range(n+1):
        print(graph[a][b], end=" ")
    print()


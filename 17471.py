import sys
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    edges[i].append(tmp[1:])

print(edges)
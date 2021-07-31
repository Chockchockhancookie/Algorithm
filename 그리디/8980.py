import heapq

n, c = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

num = 0
queue = []
for i in range(1, n+1):
    
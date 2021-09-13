import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

count = 0
for _ in range(m):
    a, b = map(int, input().split())
    if parent(parent, a) != parent(parent, b):
        union_parent(parent, a, b)
        count += 1

graph = []
for i in range(1, n + 1):
    for j in range(i + 1, n):
        graph.append((i, j, dist(data[i], data[j])))

graph.sort(key=lambda x: x[2])
for i in graph:
    if find_parent(parent, i[0]) != find_parent(parent, i[1]):
        union_parent(parent, i[0], i[1])

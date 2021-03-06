import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
s, e = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort(reverse=True)

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

answer = int(1e9)
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        if find_parent(parent, s) == find_parent(parent, e):
            print(cost)
            sys.exit()

print(0)
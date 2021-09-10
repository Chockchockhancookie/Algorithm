import sys
input = sys.stdin.readline


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

edges = []
sum_value = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
    sum_value += c

edges.sort()

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

count = 0
answer = 0
for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        answer += cost
        count += 1

if count == n-1:
    print(sum_value - answer)
else:
    print(-1)
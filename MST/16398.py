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


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

edges = []
for a in range(n):
    for b in range(a, n):
        if a == b:
            continue
        edges.append([graph[a][b], a, b])

edges.sort()

parent = [0] * (n+1)
for a in range(n):
    parent[a+1] = a+1

answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a+1) != find_parent(parent, b+1):
        answer += cost
        union_parent(parent, a+1, b+1)

print(answer)
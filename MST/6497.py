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


answer = []

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    edges = []
    total = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        edges.append([c, a, b])
        total += c

    parent = [0] * m
    for i in range(m):
        parent[i] = i

    edges.sort()

    check = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            check += cost

    answer.append(total - check)

for i in answer:
    print(i)
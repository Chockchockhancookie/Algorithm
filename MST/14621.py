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
data = [0] + list(map(str, input().split()))

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort()

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

visited = [False] * (n+1)

answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        if data[a] != data[b]:
            union_parent(parent, a, b)
            visited[a], visited[b] = True, True
            answer += cost

check = True
for i in range(1, n+1):
    if not visited[i]:
        check = False

if check:
    print(answer)
else:
    print(-1)
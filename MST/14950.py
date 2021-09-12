import heapq
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


n, m, t = map(int, input().split())

queue = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b))

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
print(queue)
num = 0
answer = 0
while queue:
    cost, a, b = heapq.heappop(queue)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += (num*t) + cost
        num += 1

print(answer)
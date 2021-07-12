from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

def bfs(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            node = start
            next_node = edges[j][0]
            cost = edges[j][1]
            if distance[node] != INF and distance[next_node] > distance[node] + cost:
                distance[next_node] = distance[node] + cost
                if i == n-1:
                    return True
    return False


t = int(input())

answer = []
for _ in range(t):
    n, m, w = map(int, input().split())

    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges[s].append([e, t])
        edges[e].append([s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges[s].append([e, -t])

    distance = [INF] * (n+1)

    check = False
    for i in range(1, n+1):
        tmp = bfs(i)
        if tmp:
            check = True

    if check:
        answer.append("YES")
    else:
        answer.append("NO")

for i in answer:
    print(i)
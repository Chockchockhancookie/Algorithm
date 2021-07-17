import sys
input = sys.stdin.readline
INF = int(1e9)

def bellmanford():
    global check
    distance = [INF] * (n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            for node, time in edges[j]:
                if distance[node] > time + distance[j]:
                    distance[node] = time + distance[j]
                    if i == n:
                        check = False


t = int(input())

answer = []
for _ in range(t):
    n, m, w = map(int, input().split())

    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges[s].append((e, t))
        edges[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges[s].append((e, -t))

    check = True
    bellmanford()
    if check:
        answer.append("NO")
    else:
        answer.append("YES")

for i in answer:
    print(i)
import sys
input = sys.stdin.readline
INF = int(1e9)


def bellmanford(start):
    global check
    distance[start] = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            for node, dist in edges[b]:
                tmp = dist + distance[b]
                if tmp < distance[node] and distance[b] != INF:
                    distance[node] = tmp
                    if a == n:
                        check = False


n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])

distance = [INF] * (n+1)

check = True

bellmanford(1)
if check:
    for dist in distance[2:]:
        if dist != INF:
            print(dist)
        else:
            print(-1)
else:
    print(-1)
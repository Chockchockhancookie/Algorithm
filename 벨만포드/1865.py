import sys
input = sys.stdin.readline
INF = int(1e9)


def bellmanford():
    global check

    for a in range(1, n+1):
        for b in range(1, n+1):
            for node, dist in edges[b]:
                if distance[node] > dist + distance[b]:
                    distance[node] = dist + distance[b]
                    if a == n:
                        check = False
                        break


t = int(input())
answers = []
for _ in range(t):
    n, m, w = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges[s].append([e, t])
        edges[e].append([s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges[s].append([e, -t])

    check = True
    bellmanford()

    if check:
        answers.append("NO")
    else:
        answers.append("YES")

for answer in answers:
    print(answer)
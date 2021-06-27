INF = int(1e9)

t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n+2)]
    distance = [[INF] * (n+2) for _ in range(n+2)]

    for a in range(n+2):
        for b in range(n+2):
            if a == b:
                continue
            total = abs(graph[a][0] - graph[b][0]) + abs(graph[a][1] - graph[b][1])
            if total <= 1000:
                distance[a][b] = 1

    for k in range(n+2):
        for a in range(n+2):
            for b in range(n+2):
                distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

    if distance[0][n+1] < INF:
        answer.append("happy")
    else:
        answer.append("sad")

for i in answer:
    print(i)
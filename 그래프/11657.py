import sys
input = sys.stdin.readline
INF = int(1e9)


def bf(start):
    distance = [INF] * (n+1)

    distance[start] = 0
    for _ in range(n-1):
        for a in range(1, n+1):
            for i, j in edges[a]:
                if distance[i] > distance[a] + j:
                    distance[i] = distance[a] + j

    for b in range(1,  n+1):
        for i, j in edges[b]:
            if distance[i] > distance[b] + j:
                return False
    return distance


n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])

answer = bf(1)

if answer == False:
    print(-1)

else:
    for i in range(2, n+1):
        if answer[i] < INF:
            print(answer[i])
        else:
            print(-1)
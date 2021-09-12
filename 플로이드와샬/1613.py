import sys
input = sys.stdin.readline

n, k = map(int, input().split())

edges = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    edges[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if edges[i][k] and edges[k][j]:
                edges[i][j] = 1

s = int(input())

answer = []
for _ in range(s):
    s, e = map(int, input().split())
    if edges[s][e] == 1:
        answer.append(-1)
    elif edges[e][s] == 1:
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a)
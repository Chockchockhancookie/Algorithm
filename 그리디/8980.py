import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

nodes = [c] * n
graph = [list(map(int, input().split())) for _ in range(m)]
graph = sorted(graph, key=lambda x: x[1])

answer = 0
for i in range(m):
    num = c+1
    for j in range(graph[i][0], graph[i][1]):
        if nodes[j] < num:
            num = nodes[j]

    tmp = min(num, graph[i][2])
    answer += tmp

    for j in range(graph[i][0], graph[i][1]):
        nodes[j] -= tmp

print(answer)

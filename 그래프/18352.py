from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if distance[i] == INF:
                distance[i] = distance[now] + 1
                queue.append(i)

    answer = []
    for i in range(1, n+1):
        if distance[i] == k:
            answer.append(i)
    return answer


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = int(1e9)
final = bfs(x)
if not final:
    print(-1)
else:
    for i in final:
        print(i)
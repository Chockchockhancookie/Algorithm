from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visited = [False] * (n+1)
    queue = deque()
    for i in range(len(edges[start])):
        for a in edges[start][i]:
            queue.append((a, i))
    data = [start]
    while queue:
        now, num = queue.popleft()

        if now not in data:
            data.append(now)

        for x in edges[now][num]:
            if not visited[x]:
                visited[x] = True
                queue.append((x, num))

    return len(data)


n = int(input())
m = int(input())

edges = [[[], []] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a][1].append(b)
    edges[b][0].append(a)

answer = []
for i in range(1, n+1):
    answer.append(n-bfs(i))

for a in answer:
    print(a)
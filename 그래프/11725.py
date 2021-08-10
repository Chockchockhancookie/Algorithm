from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    visited[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i in edges[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] = now
                queue.append(i)


n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

answer = [0] * (n+1)

bfs(1)

for i in range(2, n+1):
    print(answer[i])
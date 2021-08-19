from collections import deque
import sys
input = sys.stdin.readline


def bfs(weight):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i in edges[now]:
            if not visited[i[0]] and i[1] >= weight:
                visited[i[0]] = True
                queue.append(i[0])

    if visited[end]:
        return True
    else:
        return False


n, m = map(int, input().split())

edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

start, end = map(int, input().split())

left = 1
right = 1000000000
answer = 0
while left <= right:
    mid = (left+right)//2
    if bfs(mid):
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(answer)
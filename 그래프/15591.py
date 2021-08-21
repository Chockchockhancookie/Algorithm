from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize


def bfs(start, num):
    distance = [INF] * (n+1)
    visited = [False] * (n+1)
    visited[start] = True
    queue = deque()
    queue.append((INF, start))
    count = 0
    while queue:
        dist, now = queue.popleft()
        for i in edges[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                cost = min(dist, i[1])
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    queue.append((cost, i[0]))
    count = 0
    for i in range(1, n+1):
        if i != start and distance[i] >= num:
            count += 1

    return count


n, q = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

answers = []
for _ in range(q):
    k, v = map(int, input().split())
    answers.append(bfs(v, k))

for answer in answers:
    print(answer)
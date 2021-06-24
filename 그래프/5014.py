from collections import deque
import sys
INF = int(1e9)
input = sys.stdin.readline

def bfs(start):
    distance = [INF] * (f+1)
    distance[start] = 0
    queue = deque()
    queue.append((0, start))
    while queue:
        dist, now = queue.popleft()
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                queue.append((cost, i[0]))
    return distance[g]


f, s, g, u, d = map(int, input().split())   # 건물 층수, 강호의 위치, 스타링크 층, 업버튼, 다운버튼
graph = [[] for _ in range(f+1)]

for i in range(1, f+1):
    if i + u <= f:
        graph[i].append((i+u, 1))
    if i - d >= 1:
        graph[i].append((i-d, 1))

result = bfs(s)
if result >= INF:
    print("use the stairs")
else:
    print(result)
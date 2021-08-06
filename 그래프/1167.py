from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)


def bfs(start):
    visited = [-1] * (v+1)
    visited[start] = 0
    queue = deque()
    queue.append(start)
    node, dist = 0, 0
    while queue:
        now = queue.popleft()
        for i in edges[now]:
            if visited[i[0]] == -1:
                visited[i[0]] = visited[now] + i[1]
                queue.append(i[0])

                if dist < visited[i[0]]:
                    node = i[0]
                    dist = visited[i[0]]
    return node, dist


v = int(input())

edges = [[] for _ in range(v+1)]
for _ in range(v):
    data = list(map(int, input().split()))[:-1]
    num = data.pop(0)
    for i in range(0, len(data), 2):
        edges[num].append([data[i], data[i+1]])

node1, distance1 = bfs(1)
node2, distance2 = bfs(node1)
print(distance2)


from collections import deque
import sys
input = sys.stdin.readline


def find_node(start):
    distance = [-1] * (n+1)
    distance[start] = 0
    queue = deque()
    queue.append((0, start))
    while queue:
        dist, now = queue.popleft()
        for i in edges[now]:
            if distance[i[0]] == -1:
                cost = dist + i[1]
                distance[i[0]] = cost
                queue.append((cost, i[0]))

    return distance


n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

data = find_node(1)
node = data.index(max(data))

print(max(find_node(node)))
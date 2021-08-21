from collections import deque
import sys
input = sys.stdin.readline

n, k, r = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
road = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r):
    w, x, y, z = map(int, input().split())
    road[w][x].append([y, z])
    road[y][z].append([w, x])

cow = []
for _ in range(k):
    x, y = map(int, input().split())
    cow.append([x, y])
    graph[x][y] = True

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = 0
for a, b in cow:
    if graph[a][b]:
        visited = [[True] * (n+1) for _ in range(n+1)]
        queue = deque()
        queue.append((a, b))
        graph[a][b] = False
        count = 0
        k -= 1
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 < nx <= n and 0 < ny <= n and visited[nx][ny]:
                    if [nx, ny] not in road[x][y]:
                        queue.append((nx, ny))
                        visited[nx][ny] = False
                        if graph[nx][ny]:
                            count += 1
        answer += (k-count)

print(answer)
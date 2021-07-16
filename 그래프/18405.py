from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, virus_x, virus_y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

data = []
for a in range(n):
    for b in range(n):
        if graph[a][b] != 0:
            data.append((graph[a][b], a, b, 0)) # 바이러스 숫자가 낮은 것부터 우선시 하기 위해서!!!!

data.sort()             # 바이러스 숫자가 낮은 것부터 우선시 하기 위해서!!!!
queue = deque(data)

while queue:
    virus, x, y, second = queue.popleft()
    if second == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, nx, ny, second + 1))

print(graph[virus_x-1][virus_y-1])
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize


def bfs(x, y, broke):
    distance[x][y][0] = 0
    queue = deque()
    queue.append((x, y, broke))
    while queue:
        x, y, z = queue.popleft()
        if x == end_x-1 and y == end_y-1:
            return distance[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    if nz:
                        continue
                    else:
                        nz = 1

                if distance[nx][ny][nz] == -1:
                    distance[nx][ny][nz] = distance[x][y][z] + 1
                    queue.append((nx, ny, nz))

    return -1


n, m = map(int, input().split())
start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

distance = [[[-1, -1] for _ in range(m)] for _ in range(n)]

print(bfs(start_x-1, start_y-1, 0))

for a in range(n):
    for b in range(m):
        print(distance[a][b], end=" ")
    print()
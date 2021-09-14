from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    distance = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    distance[0][0][0] = 0
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, z = queue.popleft()

        if x == n-1 and y == m-1:
            return distance[x][y][z]+1

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
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

print(bfs())
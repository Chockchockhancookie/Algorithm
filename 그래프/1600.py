from collections import deque


def bfs():
    visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append((0, 0, k))
    while queue:
        x, y, z = queue.popleft()
        if x == h-1 and y == w-1:
            return visited[x][y][z]
        if z > 0:
            for i in range(8):
                nx = x + horse_dx[i]
                ny = y + horse_dy[i]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and visited[nx][ny][z-1] == 0:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z-1))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

horse_dx = [-1, -1, -2, -2, 1, 1, 2, 2]
horse_dy = [-2, 2, -1, 1, -2, 2, -1, 1]

print(bfs())
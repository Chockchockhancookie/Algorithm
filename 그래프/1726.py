from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, direction, count):
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    queue = deque()
    queue.append((x, y, direction, count))
    while queue:
        x, y, direction, count = queue.popleft()
        if x == end_x + 1 and y == end_y + 1:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not visited[nx][ny]:
                if direction != i:
                    if abs(direction-i) == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny, i, count + 2))
                    else:
                        visited[nx][ny] = True
                        queue.append((nx, ny, i, count + 1))
                else:
                    visited[nx][ny] = True
                    queue.append((nx, ny, i, count))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y, start_direction = map(int, input().split())
end_x, end_y, end_direction = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

start_direction %= 4

count = 0
print(bfs(start_x-1, start_y-1, start_direction, count))
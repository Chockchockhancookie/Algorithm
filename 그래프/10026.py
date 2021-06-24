from collections import deque


def bfs(x, y, color):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def bfs_color(x, y, check):
    visited_color[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check:
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == "B":
                    if not visited_color[nx][ny]:
                        visited_color[nx][ny] = True
                        queue.append((nx, ny))
            else:
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == "R" or graph[nx][ny] == "G":
                        if not visited_color[nx][ny]:
                            visited_color[nx][ny] = True
                            queue.append((nx, ny))


n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited_color = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
num = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            bfs(x, y, graph[x][y])
            count += 1

        if not visited_color[x][y]:
            if graph[x][y] == "B":
                check = True
            else:
                check = False
            bfs_color(x, y, check)
            num += 1

print(count, num)
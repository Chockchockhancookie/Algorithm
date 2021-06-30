from collections import deque


def dfs(x, y):
    distance = [[-1] * m for _ in range(n)]
    distance[x][y] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == "#":
                    distance[nx][ny] = distance[x][y] + 1
                    return distance[x2-1][y2-1]
                elif graph[nx][ny] == "1" and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == "0" and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y]
                    queue.appendleft((nx, ny))


n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = dfs(x1-1, y1-1)

print(answer)
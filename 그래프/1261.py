from collections import deque


def bfs(x, y):
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
                if distance[nx][ny] == -1:
                    if graph[nx][ny] == 1:
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx, ny))
                    elif graph[nx][ny] == 0:
                        distance[nx][ny] = distance[x][y]
                        queue.appendleft((nx, ny))		# 0인 값부터 queue에서 나와  최소 수로 결과값을 나오게 한다.
    return distance


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = bfs(0, 0)
print(result[n-1][m-1])
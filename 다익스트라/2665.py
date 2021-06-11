from collections import deque
INF = int(1e9)


def bfs():
    visited = [[INF] * n for _ in range(n)]
    visited[0][0] = 0
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, cost = queue.popleft()
        print(x, y, cost)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                temp = cost + 1
                if visited[nx][ny] < temp:
                    continue
                queue.append((nx, ny, temp))
            else:
                if visited[nx][ny] < cost:
                    continue
                else:
                    visited[nx][ny] = cost
                    queue.append((nx, ny, cost))
    return visited[n-1][n-1]


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs())
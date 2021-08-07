from collections import deque


def bfs(a, b, txt):
    visited = [[False] * m for _ in range(n)]
    visited[a][b] = True
    queue = deque()
    queue.append((a, b, txt))
    if graph[a][b] != txt:
        count = 1
    else:
        count = 0
    while queue:
        x, y, color = queue.popleft()
        if color == "B":
            tmp = "W"
        else:
            tmp = "B"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if a <= nx < a+8 and b <= ny < b+8 and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] != tmp:
                    count += 1
                    queue.append((nx, ny, tmp))
                else:
                    queue.append((nx, ny, tmp))
    return count


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = int(1e9)
for a in range(n - 7):
    for b in range(m - 7):
        black = bfs(a, b, "B")
        white = bfs(a, b, "W")
        answer = min(answer, black, white)

print(answer)
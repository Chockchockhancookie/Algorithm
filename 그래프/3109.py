import sys
input = sys.stdin.readline


def pipeline(x, y):
    if y == m-1:
        return True

    for i in range(3):
        nx = x + dx[i]
        if 0 <= nx < n and graph[nx][y+1] == "." and not visited[nx][y+1]:
            visited[nx][y+1] = True
            if pipeline(nx, y+1):
                return True
    return False


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1]

answer = 0
for i in range(n):
    if graph[i][0] == ".":
        if pipeline(i, 0):
            answer += 1

print(answer)
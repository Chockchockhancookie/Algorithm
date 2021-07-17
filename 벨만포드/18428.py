from itertools import combinations
import sys
input = sys.stdin.readline


def dfs(x, y, direct_x, direct_y):
    nx = x + direct_x
    ny = y + direct_y
    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == "X":
            dfs(nx, ny, direct_x, direct_y)
        elif graph[nx][ny] == "O":
            return False
        elif graph[nx][ny] == "S":
            return True
    return False


n = int(input())
graph = [list(input().split()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

data = []
teachers = []

for a in range(n):
    for b in range(n):
        if graph[a][b] == "X":
            data.append((a, b))
        elif graph[a][b] == "T":
            teachers.append((a, b))

answer = False
for ch in combinations(data, 3):
    for x, y in ch:
        graph[x][y] = "O"

    check = True
    for x, y in teachers:
        tmp = False
        for i in range(4):
            tmp = dfs(x, y, dx[i], dy[i])
            print(ch, tmp)
        if tmp:
            check = False

    if check:
        answer = True

if answer:
    print("YES")
else:
    print("NO")
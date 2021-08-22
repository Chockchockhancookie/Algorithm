import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
tmp = [["O"] * c for _ in range(r)]
while count <= n:
    count += 1
    if count == 1:
        continue
    if count % 2 == 1:
        for x in range(r):
            for y in range(c):
                if graph[x][y] == "O":
                    tmp[x][y] = "."
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < r and 0 <= ny < c and tmp[nx][ny] == "O":
                            tmp[nx][ny] = "."
        graph = tmp
        tmp = [["O"] * c for _ in range(r)]

if n % 2 == 0:
    graph = tmp

for a in range(r):
    for b in range(c):
        print(graph[a][b], end="")
    print()
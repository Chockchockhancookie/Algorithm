from collections import deque


def bfs():
    global j, fire
    while j:
        temp = deque()
        while j:
            x, y = j.popleft()
            if (x == r-1 or y == c-1 or x == 0 or y == 0) and graph[x][y] != "F":
                return graph[x][y] + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "F" and graph[nx][ny] == ".":
                    temp.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1

        j = temp

        if not j:
            break

        temp = deque()
        while fire:
            x, y = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "$" and visited[nx][ny] == 0:
                    temp.append([nx, ny])
                    visited[nx][ny] = 1
                    graph[nx][ny] = "F"
        fire = temp


r, c = map(int, input().split())
graph = []

j = deque()
fire = deque()
visited = [[0] * c for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for a in range(r):
    tmp = list(input())
    graph.append(tmp)
    for b in range(c):
        if tmp[b] == "J":
            j.append([a, b])
            graph[a][b] = 0
        elif tmp[b] == "F":
            fire.append([a, b])
            visited[a][b] = 1

answer = bfs()
if answer != None:
    print(answer)
else:
    print("IMPOSSIBLE")

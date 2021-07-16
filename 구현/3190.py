def move_direction(word):
    global direction
    if word == "D":
        direction += 1
        if direction == 4:
            direction = 0
    elif word == "L":
        direction -= 1
        if direction == -1:
            direction = 3


def simulation():
    x, y = 1, 1
    graph[x][y] = 2
    time = 0
    idx = 0
    queue = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 2:
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 2
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
                a, b = queue.pop(0)
                graph[a][b] = 0
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        if idx < l and time == data[idx][0]:
            move_direction(data[idx][1])
            idx += 1
    return time


n = int(input())
k = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

l = int(input())

data = []
for _ in range(l):
    t, d = map(str, input().split())
    data.append([int(t), d])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

print(simulation())
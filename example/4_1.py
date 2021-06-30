n = int(input())
data = list(input())

x, y = 0, 0

move = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for direct in data:
    for i in range(4):
        if direct == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                x, y = nx, ny

print(x+1, y+1)
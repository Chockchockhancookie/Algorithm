def move_wall(x, y):
    global answer
    nx = x - 1
    ny = y
    if nx == human_x and ny == human_y:
        answer = 0


def dfs(x, y):


graph = [list(input()) for _ in range(8)]
human_x, human_y = 7, 0
answer = 1,
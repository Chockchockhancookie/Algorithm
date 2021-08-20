import sys
input = sys.stdin.readline


def move_dice(arr, x):
    if x == 1:
        return [0, arr[3], arr[2], arr[6], arr[1], arr[5], arr[4]]
    elif x == 2:
        return [0, arr[4], arr[2], arr[1], arr[6], arr[5], arr[3]]
    elif x == 3:
        return [0, arr[2], arr[6], arr[3], arr[4], arr[1], arr[5]]
    else:
        return [0, arr[5], arr[1], arr[3], arr[4], arr[6], arr[2]]


n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

directions = list(map(int, input().split()))    # 동쪽-1, 서쪽-2, 북쪽-3, 남쪽-4

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

dices = [0] * 7

answers = []
for direct in directions:
    if direct == 4:
        direct = 0
    nx = x + dx[direct]
    ny = y + dy[direct]
    if 0 <= nx < n and 0 <= ny < m:
        dices = move_dice(dices, direct)
        answers.append(dices[1])
        if graph[nx][ny] == 0:
            graph[nx][ny] = dices[6]
        else:
            dices[6] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(dices[1])
from copy import deepcopy
import sys
input = sys.stdin.readline


def dfs(data, cnt):
    global answer
    array = deepcopy(data)

    if cnt == count:
        num = 0
        for k in array:
            num += k.count(0)
        answer = min(answer, num)
        return

    x, y, number = cctv[cnt]
    for direct in directions[number]:
        find_people(x, y, direct, array)
        dfs(array, cnt+1)
        array = deepcopy(data)


def find_people(x, y, direct, arr):
    for i in direct:
        tmp_x, tmp_y = x, y
        while True:
            nx = tmp_x + dx[i]
            ny = tmp_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = "-"
            else:
                break
            tmp_x, tmp_y = nx, ny


directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [2, 1], [1, 3], [3, 0]],
    [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = []
cctv = []

count = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] != 0 and tmp[j] != 6:
            count += 1
            cctv.append([i, j, tmp[j]])

answer = int(1e9)
dfs(graph, 0)

print(answer)


# slicing과 deepcopy의 차이!
#
# 슬라이싱의 경우에는
# array = data[:]하고 array 값을 바꿔주면 data에도 영향을 끼친다.
#
# 반면에 deepcopy는
# array = deepcopy(data)를 하고 array 값을 바꿔줘도 data에는 영향을 끼치지 않는다!!
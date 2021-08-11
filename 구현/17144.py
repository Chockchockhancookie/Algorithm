from copy import deepcopy
import sys
input = sys.stdin.readline


def spread_dust(array):     # 미세먼지 확산
    edges = [[0] * c for _ in range(r)]
    for a in range(r):
        for b in range(c):
            if array[a][b] != 0 and array[a][b] != -1:
                left = array[a][b]
                num = array[a][b] // 5
                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and array[nx][ny] != -1:
                        edges[nx][ny] += num
                        left -= num
                edges[a][b] += left
            if array[a][b] == -1:
                edges[a][b] = -1
    return edges


def remove_dust(arr):       # 미세먼지 제거
    data = deepcopy(arr)
    for i in range(2):
        x, y = air[i]
        arr[x][y] = 0
        if i == 0:
            for k in range(0, x+1):
                if k != 0:
                    data[k][0] = arr[k-1][0]
                if k != x+1:
                    data[k][-1] = arr[k+1][-1]
            for k in range(0, c):
                if k != 0:
                    data[x][k] = arr[x][k-1]
                if k != c-1:
                    data[0][k] = arr[0][k+1]
        else:
            for k in range(x, r):
                if k != r-1:
                    data[k][0] = arr[k+1][0]
                if k != x:
                    data[k][-1] = arr[k-1][-1]
            for k in range(0, c):     # 위
                if k != 0:
                    data[x][k] = arr[x][k-1]
                if k != c-1:
                    data[-1][k] = arr[-1][k+1]

        data[x][y] = -1

    return data


r, c, t = map(int, input().split())
graph = []
air = []

for a in range(r):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for b in range(c):
        if tmp[b] == -1:
            air.append([a, b])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    graph = spread_dust(graph)
    graph = remove_dust(graph)

answer = 0
for a in range(r):
    answer += sum(graph[a])

print(answer+2)
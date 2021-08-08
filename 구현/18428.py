from collections import deque
from itertools import combinations
from copy import deepcopy


def bfs(a, b, data):
    queue = deque()
    visited[a][b] = True
    for direct in range(4):
        queue.append((a, b, direct))

    while queue:
        x, y, direction = queue.popleft()
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == "O":
                continue
            else:
                visited[nx][ny] = True
                queue.append((nx, ny, direction))


n = int(input())
graph = []

teachers = []
students = []
spaces = []

for i in range(n):
    tmp = list(input().split())
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == "T":
            teachers.append([i, j])
        elif tmp[j] == "S":
            students.append([i, j])
        else:
            spaces.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


answer = "NO"
for space in combinations(spaces, 3):
    data = deepcopy(graph)
    visited = [[False] * n for _ in range(n)]
    for x, y in space:
        data[x][y] = "O"

    for x, y in teachers:
        bfs(x, y, data)

    cnt = 0
    for x, y in students:
        if not visited[x][y]:
           cnt += 1
    if cnt == len(students):
        answer = "YES"

print(answer)
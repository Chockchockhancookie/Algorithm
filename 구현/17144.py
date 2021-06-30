from copy import deepcopy


def divide():
     tmp = [[0] * c for _ in range(r)]
     tmp[air1_x][0] = -1
     tmp[air2_x][0] = -1
     for i in range(r):
          for j in range(c):
               if graph[i][j] > 0:
                    count = 0
                    for k in range(4):
                         x = i + dx[k]
                         y = j + dy[k]
                         if 0 <= x < r and 0 <= y < c and graph[x][y] != -1:
                              tmp[x][y] += graph[i][j] // 5
                              count += 1
                    tmp[i][j] += graph[i][j] - (graph[i][j] // 5 * count)
     return tmp


def clear(x, y, dir):
     temp = deepcopy(graph)
     cx, cy = x, y-1
     graph[x][y] = 0
     for i in range(4):
          while True:
               nx = x + dx[dir[i]]
               ny = y + dy[dir[i]]
               if nx == cx and ny == cy:
                    return
               if 0 <= nx < r and 0 <= ny < c:
                    graph[nx][ny] = temp[nx][ny]
               else:
                    break
               x, y = nx, ny


r, c, t = map(int, input().split())
graph = []

air = -1
for i in range(r):
     tmp = list(map(int, input().split()))
     for a in tmp:
          if a == -1 and air == -1:
               air = i
     graph.append(tmp)

air1_x, air1_y = air, 0
air2_x, air2_y = air+1, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(t):
      graph = divide()
      clear(air1_x, air1_y+1, [3, 1, 2, 0])
      clear(air2_x, air2_y+1, [3, 1, 2, 0])


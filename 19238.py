import sys
input = sys.stdin.readline

n, m, f = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

start = []
destination = []
for _ in range(m):
    a, b, c, d = map(int, input().split())
    start.append((a, b))
    destination.append((c, d))

while True:
    i, j = -1, -1
    num = int(1e9)
    for i in range(m):
        for tmp_x, tmp_y in start[i]:
            tmp = abs(x-tmp_x) + abs(y-tmp_y)
            if tmp < num:
                i, j = tmp_x, tmp_y
            elif tmp == num:
                if tmp_x < i:
                    i, j = tmp_x, tmp_y
                elif tmp_x == i:
                    if tmp_y < j:
                        i, j = tmp_x, tmp_y


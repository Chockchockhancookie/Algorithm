import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(h+x)]
array_A = [[0] * w for _ in range(h)]

for a in range(h):
    for b in range(w):
        if 0 <= a-x < h and 0 <= b-y < w:
            array_A[a][b] = graph[a][b] - array_A[a-x][b-y]
        else:
            array_A[a][b] = graph[a][b]

for a in range(h):
    for b in range(w):
        print(array_A[a][b], end=" ")
    print()
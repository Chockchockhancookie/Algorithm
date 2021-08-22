import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y, z = map(int, input().split())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


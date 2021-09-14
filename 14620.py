import sys
input = sys.stdin.readline


def bfs(x, y):



n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

count = 0
for a in range(1, n-1):
    for b in range(1, n-1):
        bfs(a, b)
import sys
input = sys.stdin.readline

n, m, f = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

person = []
for _ in range(m):
    
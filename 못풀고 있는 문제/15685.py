import sys
input = sys.stdin.readline

n = int(input())
curve = []
for _ in range(n):
    x, y, d, g = map(int, input().split())  # x, y는 드래곤 커브 시작점, 방향, 세대
    
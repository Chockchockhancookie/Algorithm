import sys
input = sys.stdin.readline

n = int(input())
curve = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
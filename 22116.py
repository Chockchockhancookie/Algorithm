import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

answer = int(1e9)

if answer == int(1e9):
    print(0)
else:
    print(answer)
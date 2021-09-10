import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

start_x, start_y, start_direction = map(int, input().split())
end_x, end_y, end_direction = map(int, input().split())

distance = [[0] * m for _ in range(n)]

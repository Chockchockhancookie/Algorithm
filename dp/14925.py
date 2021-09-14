# from collections import deque
# import sys
# input = sys.stdin.readline
#
#
# def bfs(x, y, cnt):
#     queue = deque()
#     queue.append([x, y, cnt])
#     while queue:
#         x, y, cnt = queue.popleft()
#
#         for i in range(3):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] != 0:
#                     return cnt
#                 else:
#                     queue.append([nx, ny, cnt+1])
#             else:
#                 return cnt
#     return cnt
#
#
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [1, 0, 1]
# dy = [0, 1, 1]
#
# answer = -1
# for a in range(n):
#     for b in range(m):
#         if graph[a][b] == 0:
#             answer = max(answer, bfs(a, b, 1))
#
# print(answer)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

answer = -1
for a in range(n):
    for b in range(m):
        if graph[a][b] == 0:
            dp[a][b] = min(dp[a-1][b], dp[a][b-1], dp[a-1][b-1]) + 1
    answer = max(answer, max(dp[a]))

print(answer)
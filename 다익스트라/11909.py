import sys
input = sys.stdin.readline

#dp로 풀자!
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp =[[0] * n for _ in range(n)]
dp[0][0] = 0

for a in range(n):
    for b in range(n):
        if a == 0 and b == 0:
            continue
        left, up = 0, 0
        left_x, left_y, up_x, up_y = a, b-1, a-1, b
        if 0 <= left_x < n and 0 <= left_y < n:
            if graph[left_x][left_y] > graph[a][b]:
                left = dp[left_x][left_y]
            else:
                left = dp[left_x][left_y] + (graph[a][b] - graph[left_x][left_y] + 1)
        else:
            left = int(1e9)

        if 0 <= up_x < n and 0 <= up_y < n:
            if graph[up_x][up_y] > graph[a][b]:
                up = dp[up_x][up_y]
            else:
                up = dp[up_x][up_y] + (graph[a][b] - graph[up_x][up_y] + 1)
        else:
            up = int(1e9)

        dp[a][b] = min(left, up)

print(dp[n-1][n-1])
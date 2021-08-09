import sys
input = sys.stdin.readline


def max_value():
    max_dp = [[0] * n for _ in range(n)]

    for i in range(n):
        max_dp[0][i] = graph[0][i]

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                max_dp[i][j] = max(max_dp[i][j], max_dp[i - 1][j] + graph[i][j], max_dp[i - 1][j + 1] + graph[i][j])
            elif j == n - 1:
                max_dp[i][j] = max(max_dp[i][j], max_dp[i - 1][j] + graph[i][j], max_dp[i - 1][j - 1] + graph[i][j])
            else:
                max_dp[i][j] = max(max_dp[i][j], max_dp[i - 1][j] + graph[i][j], max_dp[i - 1][j + 1] + graph[i][j], max_dp[i - 1][j - 1] + graph[i][j])

    return max(max_dp[n-1])


def min_value():
    min_dp = [[int(1e9)] * n for _ in range(n)]

    for i in range(n):
        min_dp[0][i] = graph[0][i]

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                min_dp[i][j] = min(min_dp[i][j], min_dp[i - 1][j] + graph[i][j], min_dp[i - 1][j + 1] + graph[i][j])

            elif j == n - 1:
                min_dp[i][j] = min(min_dp[i][j], min_dp[i - 1][j] + graph[i][j], min_dp[i - 1][j - 1] + graph[i][j])

            else:
                min_dp[i][j] = min(min_dp[i][j], min_dp[i - 1][j] + graph[i][j], min_dp[i - 1][j + 1] + graph[i][j], min_dp[i - 1][j - 1] + graph[i][j])

    return min(min_dp[n - 1])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer1 = max_value()
answer2 = min_value()

print(answer1, answer2)
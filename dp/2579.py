n = int(input())
data = [int(input()) for _ in range(n)]

dp = [[0, 0] for _ in range(n)]

if n == 1:
    dp[0][0], dp[0][1] = data[0], data[0]
elif n == 2:
    dp[0][0], dp[0][1] = data[0], data[0]
    dp[1][0], dp[1][1] = data[0] + data[1], data[1]
else:
    dp[0][0], dp[0][1] = data[0], data[0]
    dp[1][0], dp[1][1] = data[0] + data[1], data[1]

    for i in range(2, n):
        dp[i][0] = dp[i-1][1] + data[i]
        dp[i][1] = max(dp[i-2][1], dp[i-2][0]) + data[i]

print(max(dp[n-1][0], dp[n-1][1]))
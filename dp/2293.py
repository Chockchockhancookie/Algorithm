n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for num in range(1, k + 1):
        if num - coin >= 0:
            dp[num] += dp[num - coin]

print(dp[k])
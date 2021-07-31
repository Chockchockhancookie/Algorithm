import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
dp = [0] * 100001
for _ in range(n):
    coin = int(input())
    coins.append(coin)
    dp[coin] = 1

for i in range(1, k+1):
    for coin in coins:
        if i - coin > 0 and dp[i-coin] != 0:
            if dp[i] == 0:
                dp[i] = dp[i-coin] + 1
            else:
                dp[i] = min(dp[i-coin]+1, dp[i])

if dp[k] == 0:
    print(-1)
else:
    print(dp[k])
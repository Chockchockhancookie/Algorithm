import sys
input = sys.stdin.readline

data = list(map(int, input().rstrip()))
num = len(data)

dp = [0] * (num+1)
dp[0], dp[1] = 1, 1

if data[0] == 0:
    print(0)
else:
    for i in range(2, num+1):
        if data[i-1] > 0:
            dp[i] += dp[i-1]
        tmp = data[i-1] + 10 * data[i-2]
        if 10 <= tmp <= 26:
            dp[i] += dp[i-2]
    print(dp[num] % 1000000)

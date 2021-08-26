import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [0] * 41
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
count = 0
for i in range(m):
    vip = int(input())
    answer *= dp[vip-count-1]
    count = vip

answer *= dp[n-count]
print(answer)
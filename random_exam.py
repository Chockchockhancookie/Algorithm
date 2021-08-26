import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

vip = list(int(input()) for _ in range(m))

dp = [0] * (n+1)
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
if m >= 1:
    count = 0
    for i in vip:
        answer *= dp[i-count-1]
        count = i
    answer *= dp[n-count]
else:
    answer = dp[n]
print(answer)
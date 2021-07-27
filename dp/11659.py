import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = data[1]

answers = []
for i in range(2, n+1):
    dp[i] = dp[i-1] + data[i]

for _ in range(m):
    i, j = map(int, input().split())
    answers.append(dp[j]-dp[i-1])

for answer in answers:
    print(answer)
import copy
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = copy.deepcopy(data)
for a in range(1, n):
    for b in range(a+1):
        if b == 0:
            dp[a][b] = data[a][b] + dp[a-1][b]
        elif b == a:
            dp[a][b] = data[a][b] + dp[a-1][b-1]
        else:
            dp[a][b] = max(dp[a][b], data[a][b] + dp[a-1][b-1], data[a][b] + dp[a-1][b])

print(max(dp[n-1]))
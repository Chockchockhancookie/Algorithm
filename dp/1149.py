n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [graph[0]] + [[0] * 3 for _ in range(n-1)]

for i in range(1, n):
    for a in range(3):
        if a == 0:
            dp[i][a] = min(dp[i-1][a+1], dp[i-1][a+2]) + graph[i][a]
        elif a == 1:
            dp[i][a] = min(dp[i-1][a-1], dp[i-1][a+1]) + graph[i][a]
        elif a == 2:
            dp[i][a] = min(dp[i-1][a-2], dp[i-1][a-1]) + graph[i][a]

print(min(dp[n-1]))
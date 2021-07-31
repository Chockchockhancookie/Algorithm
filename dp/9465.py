import sys
input = sys.stdin.readline

t = int(input())

answers = []
for _ in range(t):
    n = int(input())

    sticker = []
    for i in range(2):
        sticker.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(2)]

    if n < 2:
        answers.append(max(sticker[0][0], sticker[1][0]))
    else:
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

        answers.append(max(dp[0][n-1], dp[1][n-1]))

for answer in answers:
    print(answer)
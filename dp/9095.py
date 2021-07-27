t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    if n <= 1:
        dp[1] = 1
    elif n <= 2:
        dp[1], dp[2] = 1, 2
    elif n <= 3:
        dp[1], dp[2], dp[3] = 1, 2, 4
    else:
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    answers.append(dp[n])

for answer in answers:
    print(answer)
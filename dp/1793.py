def tile(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = 2 * dp[i-2] + dp[i-1]
    return dp[n]


while True:
    try:
        print(tile(int(input())))
    except:
        break
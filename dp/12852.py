n = int(input())

dp = [0] * (n+1)
find = [0] * (n+1)

dp[1] = 0
find[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    find[i] = i-1
    if i % 3 == 0 and dp[i//3]+1 <= dp[i]:
        dp[i] = dp[i//3] + 1
        find[i] = i//3

    if i % 2 == 0 and dp[i//2]+1 <= dp[i]:
        dp[i] = dp[i//2] + 1
        find[i] = i//2


print(dp[n])
print(n, end=" ")
num = find[n]
while True:
    if num == 0:
        break
    print(num, end=" ")
    num = find[num]
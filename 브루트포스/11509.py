import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [0] * 1000001

answer = 0
for balloon in array:
    if dp[balloon]:     # 0이 아닐때 전부를 포함한다.
        dp[balloon] -= 1
        dp[balloon-1] += 1
    else:
        answer += 1
        dp[balloon-1] += 1

print(answer)

import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

data.sort()

answer = 0
for i in range(1, n+1):
    answer += abs(i-data[i-1])

print(answer)
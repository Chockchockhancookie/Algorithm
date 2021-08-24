import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

start = 0
answer = 0
while start <= n-1:
    max_value = max(data[start:])
    idx = start + data[start:].index(max_value)
    answer += max_value * (idx-start) - sum(data[start:idx])
    start = idx+1

print(answer)
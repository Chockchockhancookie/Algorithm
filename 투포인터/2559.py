import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))


sum_value = sum(data[:k])

answer = sum_value
for i in range(k, n):
    tmp = sum_value - data[i-k] + data[i]
    sum_value = tmp
    answer = max(answer, tmp)

print(answer)
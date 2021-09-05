import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

sum_value = [0] * (n+1)
for i in range(1, n+1):
    sum_value[i] = sum_value[i-1] + data[i-1]

answer = int(1e9)
start, end = 0, 1
while start < n:
    if sum_value[end] - sum_value[start] >= s:
        answer = min(answer, end - start)
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1

if answer == int(1e9):
    print(0)
else:
    print(answer)
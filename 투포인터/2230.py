import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()

start, end = 0, 1
answer = sys.maxsize

while start < n and end < n:
    tmp = data[end] - data[start]
    if tmp == m:
        print(m)
        sys.exit()

    if tmp < m:
        end += 1
        continue

    start += 1
    answer = min(answer, tmp)

print(answer)
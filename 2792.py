import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(m)]

start, end = 1, max(data)

answer = int(1e9)
while start <= end:
    count = 0
    mid = (start+end) // 2
    for jew in data:
        count += math.ceil(jew/mid)

    if count > n:
        start = mid+1
    else:
        end = mid-1
        answer = min(answer, mid)

print(answer)
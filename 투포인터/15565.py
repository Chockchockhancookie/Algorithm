import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
answer = sys.maxsize
count = 0
while start < n:
    print(start, end, count)

    if count == 3:
        answer = min(end-start, answer)
        count -= 1
        start += 1
        continue
    else:
        if data[end] == 1:
            count += 1


print(answer)
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

answer1, answer2 = 0, 0
start, end = 0, n-1
min_value = sys.maxsize

while start < end:
    tmp = data[start]+data[end]

    if abs(tmp) < min_value:
        min_value = abs(tmp)
        answer1, answer2 = data[start], data[end]

    if tmp < 0:
        start += 1
    elif tmp > 0:
        end -= 1
    else:
        break

print(answer1, answer2)
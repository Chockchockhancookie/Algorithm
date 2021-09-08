import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = 0
for i in range(n - 2):
    start, end = i + 1, n - 1
    max_idx = n
    while start < end:
        tmp = data[i] + data[start] + data[end]
        if tmp == 0:
            if data[start] == data[end]:
                answer += (end - start)
            else:
                if max_idx > end:
                    max_idx = end
                    while max_idx >= 0 and data[max_idx-1] == data[end]:
                        max_idx -= 1
                answer += (end-max_idx+1)
            start += 1
        elif tmp < 0:
            start += 1
        else:
            end -= 1

print(answer)

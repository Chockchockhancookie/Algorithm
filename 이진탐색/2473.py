import sys
input = sys.stdin.readline


def find_number(x):
    number = data[x]
    start = x+1
    end = n-1
    min_value = sys.maxsize
    answer1, answer2 = 0, 0
    while start < end:
        tmp = data[start]+data[end]+number
        if abs(tmp) < abs(min_value):
            min_value = tmp
            answer1 = data[start]
            answer2 = data[end]
            if tmp == 0:
                return number, answer1, answer2
        if tmp > 0:
            end -= 1
        else:
            start += 1
    return number, answer1, answer2


n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = None
sum_value = sys.maxsize
for i in range(n-2):
    left, middle, right = find_number(i)
    if abs(left+middle+right) < abs(sum_value):
        sum_value = left+right+middle
        answer = [left, middle, right]

for i in answer:
    print(i, end=" ")
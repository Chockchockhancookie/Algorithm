import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

start = 0
end = n-1

answer = data[start] + data[end]
answer_left, answer_right = start, end

while start < end:
    num = data[start] + data[end]
    if abs(num) < abs(answer):
        answer = num
        answer_left = start
        answer_right = end
        if answer == 0:
            break
    if num < 0:
        start += 1
    else:
        end -= 1

print(data[answer_left], data[answer_right])
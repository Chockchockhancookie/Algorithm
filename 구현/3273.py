import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

x = int(input())
start = 0
end = n-1

answer = 0
while start < end:
    tmp = data[start]+data[end]
    if tmp < x:
        start += 1
    elif tmp > x:
        end -= 1
    else:
        answer += 1
        start += 1

print(answer)
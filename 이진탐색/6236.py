import sys
input = sys.stdin.readline


def count(array, x):
    tmp, cnt = 0, 0
    for money in array:
        if tmp+money > x:
            cnt += 1
            tmp = money
        else:
            tmp += money

    return cnt+1


n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

start, end = max(data), sum(data)

answer = 0
while start <= end:
    mid = (start+end)//2
    check = True
    if count(data, mid) <= m:
        end = mid-1
        answer = mid
    else:
        start = mid+1

print(answer)
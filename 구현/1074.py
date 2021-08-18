import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

answer = 0
while n > 1:
    num = (2**n) // 2

    if r < num and c < num:
        pass
    elif r < num <= c:
        answer += num**2
        c -= num
    elif c < num <= r:
        answer += num**2 * 2
        r -= num
    elif r >= num and c >= num:
        answer += num**2 * 3
        r -= num
        c -= num
    n -= 1

if r == 0 and c == 0:
    print(answer)
if r == 0 and c == 1:
    print(answer+1)
if r == 1 and c == 0:
    print(answer+2)
if r == 1 and c == 1:
    print(answer+3)
import sys
input = sys.stdin.readline

d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(1, d):        # 핵심부분이라고 생각한다.
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

answer = 0
deep = 0
start, end = 0, d-1
for p in pizza:
    check = False
    while start <= end:
        mid = (start+end) // 2
        if oven[mid] >= p:
            check = True
            start = mid+1
            answer = mid
        else:
            end = mid-1

    if not check:
        answer -= 1
        break

    start = 0
    end = answer-1

if answer == -1:
    print(0)
else:
    print(answer+1)
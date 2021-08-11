import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = [[] for _ in range(n)]

check = False
cnt = 0
for i in range(len(data)):
    if not check:
        answer[cnt].append(data[i])
        cnt += 1
        if cnt == n:
            check = True
    else:
        cnt -= 1
        answer[cnt].append(data[i])
        if cnt == 0:
            check = False

num = int(1e9)
for a in answer:
    num = min(num, sum(a))

print(num)
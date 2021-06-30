import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

distance = []
plus, minus = [], []
for i in data:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)

answer = []
plus.sort(reverse=True)
for i in range(0, len(plus), m):
    num = max(plus[i:i+m])
    answer.append(num)
for i in range(0, len(minus), m):
    num = min(minus[i:i + m])
    answer.append(abs(num))

print(2*sum(answer) - max(answer))
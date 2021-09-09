import sys
input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())

red = data.count("R")
blue = n - red

answer = min(red, blue)
count = 0

for i in range(n):
    if data[i] != data[0]:
        break
    count += 1

if data[0] == "R":
    answer = min(answer, red - count)
else:
    answer = min(answer, blue - count)

cnt = 0
for i in range(n-1, -1, -1):
    if data[i] != data[-1]:
        break
    cnt += 1

if data[-1] == "R":
    answer = min(answer, red - cnt)
else:
    answer = min(answer, blue - cnt)

print(answer)
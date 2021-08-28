import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())    # 트럭의 수, 다리길이, 최대하중
trucks = list(map(int, input().split()))
data = [0] * n

weight = 0
start, end = 0, 0
time = 0
while True:
    if data[-1] > w:
        break

    for i in range(start, end):
        if data[i] < w+1:
            data[i] += 1
        if data[start] > w:
            weight -= trucks[start]
            start += 1

    if end < n and weight + trucks[end] <= l:
        weight += trucks[end]
        data[end] += 1
        end += 1

    time += 1

print(time)
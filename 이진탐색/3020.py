import sys
input = sys.stdin.readline


def binary_search(data, target):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start+end)//2
        if data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


n, h = map(int, input().split())

top = []
bottom = []

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        top.append(num)
    else:
        bottom.append(num)

top.sort()
bottom.sort()

answer = []
for i in range(1, h+1):
    up = binary_search(top, i)
    down = binary_search(bottom, h-i+1)
    answer.append(len(top)-up + len(bottom)-down)

print(min(answer), answer.count(min(answer)))
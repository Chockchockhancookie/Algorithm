import heapq
import sys
input = sys.stdin.readline

n = int(input())

arr = []
answers = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(arr) == 0:
            answers.append(0)
        else:
            now = heapq.heappop(arr)
            answers.append(now)
    else:
        heapq.heappush(arr, num)

for answer in answers:
    print(answer)
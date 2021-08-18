import heapq
import sys
input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
data = sorted(data, key=lambda x: x[1])

answer = []
for w, d in data:
    heapq.heappush(answer, w)
    if len(answer) > d:
        while len(answer) > d:
            heapq.heappop(answer)

print(sum(answer))
import heapq
import sys
input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

queue = []
heapq.heappush(queue, data[0][1])

for i in range(1,n):
    if queue[0] > data[i][0]:
        heapq.heappush(queue, data[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, data[i][1])

print(len(queue))
import heapq
import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

total = 0
while len(data) != 1:
    first = heapq.heappop(data)
    two = heapq.heappop(data)
    cost = first + two
    total += cost
    heapq.heappush(data, cost)

print(total)
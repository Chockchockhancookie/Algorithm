import heapq

n = int(input())

queue = []
day = 0
for _ in range(n):
    d, w = map(int, input().split())
    day = max(day, d)
    heapq.heappush(queue, (-w, d))

check = [False] * (day+1)

answer = 0
while queue:
    work, day = heapq.heappop(queue)
    work = -work
    while day > 0:
        if not check[day]:
            check[day] = True
            answer += work
            break
        day -= 1

print(answer)
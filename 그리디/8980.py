import heapq

n, c = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

print(graph)

num = 0
answer = 0
queue = []
for i in range(1, n+1):
    while queue:
        now, dist = heapq.heappop(queue)
        if now == i:
            answer += dist
            num -= dist
        else:
            heapq.heappush(queue, (now, dist))
            break

    for node, weight in graph[i]:
        tmp = c - num
        if tmp > 0:
            if tmp > weight:
                num += weight

                heapq.heappush( queue, (node, weight))
            else:
                num += tmp
                heapq.heappush(queue, (node, tmp
                                       ))

print(answer)
from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001
visited[n] = 0

queue = deque()
queue.append(n)
while queue:
    x = queue.popleft()
    if x == k:
        print(visited[x])
        break
    if 0 <= x - 1 < 100001 and visited[x - 1] == -1:
        visited[x - 1] = visited[x] + 1
        queue.append(x - 1)
    if 0 < 2 * x < 100001 and visited[2 * x] == -1:
        visited[2 * x] = visited[x]
        queue.appendleft(2 * x)
    if 0 < x + 1 < 100001 and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        queue.append(x + 1)

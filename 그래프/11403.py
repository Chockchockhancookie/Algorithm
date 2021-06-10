from collections import deque


def find_path(x):
    visited = [0] * (n+1)
    queue = deque()
    queue.append(x)
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    return visited[1:]


n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            graph[i].append(j+1)

answer = []
for i in range(1, n+1):
    array = find_path(i)
    answer.append(array)

for a in range(n):
    for b in range(n):
        print(answer[a][b], end=" ")
    print()

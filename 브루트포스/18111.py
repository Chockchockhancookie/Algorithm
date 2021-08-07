import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer_time = int(1e9)
answer_height = 0
for i in range(257):
    min_value, max_value = 0, 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] < i:
                min_value += (i-graph[x][y])
            else:
                max_value += (graph[x][y]-i)

    block = max_value + b

    if block < min_value:
        continue

    answer = 2*max_value + min_value
    if answer <= answer_time:
        answer_time = answer
        answer_height = i

print(answer_time, answer_height)
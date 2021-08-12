import sys
input = sys.stdin.readline


r, s = map(int, input().split())
graph = []
empty = []
people = []
for a in range(r):
    tmp = list(input().rstrip())
    graph.append(tmp)
    for b in range(s):
        if tmp[b] == ".":
            empty.append([a, b])
        elif tmp[b] == "o":
            people.append([a, b])

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

answer = 0
if len(empty) != 0:
    for x, y in empty:
        graph[x][y] = "o"
        people.append([x, y])
        count = 0
        for a, b in people:
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < r and 0 <= ny < s and graph[nx][ny] == "o":
                    count += 1
        people.pop()
        answer = max(answer, count//2)
        graph[x][y] = "."

else:
    count = 0
    for a, b in people:
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < r and 0 <= ny < s and graph[nx][ny] == "o":
                count += 1
    answer = max(answer, count // 2)

print(answer)
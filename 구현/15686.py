from itertools import combinations

INF = int(1e9)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken, house = [], []
for a in range(n):
    for b in range(n):
        if graph[a][b] == 2:
            chicken.append((a, b))
        if graph[a][b] == 1:
            house.append((a, b))

answer = int(1e9)

for ch in combinations(chicken, m):
    total = 0
    for x, y in house:
        tmp = int(1e9)
        for a, b in ch:
            tmp = min(abs(x - a) + abs(y - b), tmp)
        total += tmp
    answer = min(answer, total)

print(answer)
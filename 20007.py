import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())  # 집의 수, 도로의 수, 최대 거리, 성현이 집

edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])


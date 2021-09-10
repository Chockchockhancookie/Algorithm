from itertools import combinations
import sys
input = sys.stdin.readline


def bfs(count):
    if count == 3:
        for
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                visited[i][j] = True
                count += 1
                bfs(count)
                count -= 1
                visited[i][j] = False


n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

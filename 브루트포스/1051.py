n, m = map(int, input().split())
num = min(n, m)

graph = [list(map(int, input())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        for a in range(num):
            if i + a < n and j + a < m:		#생각하지 못한 부분!
                if graph[i][j] == graph[i+a][j] and graph[i][j] == graph[i][j+a] and graph[i][j] == graph[i+a][j+a]:
                    if count < a:
                        count = a

print((count+1)**2)
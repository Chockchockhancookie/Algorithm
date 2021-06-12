def dfs(start, visited, total):
    global count
    if total == s:
        count += 1
    if len(visited) == n:
        return
    for i in range(start+1, n):
        visited.append(i)
        dfs(i, visited, total + data[i])
        visited.pop()


n, s = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(n):
    dfs(i, [i], data[i])

print(count)
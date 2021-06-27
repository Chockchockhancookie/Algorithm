n = int(input())
data = list(map(int, input().split()))
visited = [False] * n

count = 0
for i in range(n):
    if visited[i]:
        continue
    visited[i] = True
    arrow = data[i] - 1
    count += 1
    num = i + 1
    while num < n:
        if arrow <= 0 or num >= n:
            break
        if data[num] == arrow:
            visited[num] = True
            num += 1
            arrow -= 1
        else:
            num += 1
            arrow -= 1

print(count)
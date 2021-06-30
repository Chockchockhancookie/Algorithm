import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
else:
    visited = [0] * m
    count = 0
    while True:
        for i in range(n):
            num = 0
            while num < m:
                if crane[i] >= box[num] and visited[num] == 0:
                    visited[num] = 1
                    break
                num += 1
        count += 1
        if sum(visited) == m:
            break
    print(count)
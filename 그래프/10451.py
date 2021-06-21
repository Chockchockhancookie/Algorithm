import sys
sys.setrecursionlimit(1000000)

def circle(start, purpose):
    if start == purpose:
        return
    visited[purpose] = True
    circle(start, data[purpose])


t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    count = 0
    for i in range(1, n+1):
        if not visited[i]:
            count += 1
            circle(i, data[i])

    answer.append(count)

for i in answer:
    print(i)
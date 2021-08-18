from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

answers = []
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    queue = deque()
    for i in range(n):
        queue.append((i, data[i]))

    num = max(data)
    answer = 0
    while queue:
        now, cost = queue.popleft()
        if cost == num:
            if now == m:
                answer += 1
                answers.append(answer)
                break
            else:
                answer += 1
                data[now] = 0       # 중요도가 1~9니깐
                num = max(data)
        else:
            queue.append((now, cost))

for answer in answers:
    print(answer)
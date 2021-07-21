# 텀프로젝트
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(start):
    global answer
    visited[start] = True
    queue.append(start)
    num = data[start]

    if visited[num]:
        if num in queue:
            answer += queue[queue.index(num):]  # 사이클이 되는 구간부터만 팀을 이룸
        return
    else:
        dfs(num)


t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    answer = []

    for i in range(1, n+1):
        if not visited[i]:
            queue = []
            dfs(i)

    answers.append(n-len(answer))

for ans in answers:
    print(ans)
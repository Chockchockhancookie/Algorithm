import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = list(map(int, input().split()))

num = truth.pop(0)

arrays = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    arrays.append(tmp[1:])

visited = [False] * (n+1)   # 진실을 아는 사람 체크
check = [1] * m     # 파티 체크
for i in truth:
    visited[i] = True

if num == 0:
    print(m)
else:
    while truth:
        tmp = truth.pop(0)
        for i in range(m):
            if tmp in arrays[i]:
                check[i] = 0
                for a in arrays[i]:
                    if not visited[a]:
                        visited[a] = True
                        truth.append(a)

    print(sum(check))
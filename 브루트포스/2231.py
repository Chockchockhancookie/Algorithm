import sys
input = sys.stdin.readline

n = int(input())

answer = 0
for i in range(1, n+1):
    tmp = sum(list(map(int, str(i))))
    answer = tmp + i
    if answer == n:
        print(i)
        sys.exit(0)
    if i == n:
        print(0)
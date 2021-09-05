import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for start in range(n):
    tmp = 0
    for end in range(start, n):
        tmp += data[end]
        if tmp == m:
            count += 1
            break
        elif tmp > m:
            break

print(count)
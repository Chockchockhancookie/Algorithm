import sys
input = sys.stdin.readline

t = int(input())

answer = []
for _ in range(t):
    l, n = map(int, input().split())
    locations = list(int(input()) for _ in range(n))

    min_value, max_value = 0, 0

    for i in locations:
        tmp1, tmp2 = i, l - i
        if tmp1 < tmp2:
            if min_value < tmp1:
                min_value = tmp1
            if max_value < tmp2:
                max_value = tmp2
        else:
            if min_value < tmp2:
                min_value = tmp2
            if max_value < tmp1:
                max_value = tmp1

    answer.append((min_value, max_value))

for i in answer:
    print(i[0], i[1])
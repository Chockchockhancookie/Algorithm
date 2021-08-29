import math
import sys
input = sys.stdin.readline

t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    number = [True] * (n+1)
    number[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if number[i]:
            j = 2
            while i * j <= n:
                number[i*j] = False
                j += 1
    answer1, answer2 = None, None
    start = 2
    end = n
    while start <= end:
        if not number[start]:
            start += 1
            continue
        if not number[end]:
            end -= 1
            continue

        tmp = start + end

        if tmp < n:
            start += 1
        elif tmp > n:
            end -= 1
        else:
            answer1, answer2 = start, end
            start += 1

    if answer1 is None:
        continue
    else:
        answers.append([answer1, answer2])

for x, y in answers:
    print(x, y)
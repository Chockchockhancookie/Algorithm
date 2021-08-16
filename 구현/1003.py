import sys
input = sys.stdin.readline


def fibo(num):
    tmp = len(first)
    if tmp <= num:
        for i in range(tmp, num+1):
            first.append(first[i-1] + first[i-2])
            second.append(second[i-1] + second[i-2])

    return first[num], second[num]


t = int(input())

first = [1, 0, 1]
second = [0, 1, 1]

answers = []
for _ in range(t):
    m = int(input())
    answers.append(list(fibo(m)))

for x, y in answers:
    print(x, y)
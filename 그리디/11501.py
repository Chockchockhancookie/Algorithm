import sys
input = sys.stdin.readline

t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))

    answer = 0
    num = None
    for i in range(n-1, -1, -1):
        if num is None:
            num = data[i]
        else:
            if num > data[i]:
                answer += (num-data[i])
            else:
                num = data[i]

    answers.append(answer)

for answer in answers:
    print(answer)
import sys
input = sys.stdin.readline


t = int(input())

answers = []
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    count = 0   # 이동횟수
    move = 1    # count별 빈도수
    total = 0   # 이동한 거리의 합
    while total < distance:

        count += 1
        total += move
        if count % 2 == 0:
            move += 1
        print(count, total, move)
    answers.append(count)

for answer in answers:
    print(answer)
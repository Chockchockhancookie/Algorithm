import sys
input = sys.stdin.readline

t = int(input())

answer = []
for _ in range(t):
    data = list(input())                    # R은 뒤집기 D는 버리기!
    n = int(input())
    array = input()[1:-2].split(",")        # 기억하자!!

    rev = 0
    forward, back = 0, 0
    for txt in data:
        if txt == "R":
            rev += 1
        elif txt == "D":
            if rev % 2 == 0:
                forward += 1
            else:
                back += 1

    if forward + back <= n:
        array = array[forward:n-back]
        if rev % 2 == 1:
            answer.append("[" + ",".join(array[::-1]) + "]")
        else:
            answer.append("[" + ",".join(array) + "]")
    else:
        answer.append("error")

for i in answer:
    print(i)
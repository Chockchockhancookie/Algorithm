answers = []
while True:
    num = list(map(int, input()))
    if num[0] == 0:
        break

    check = True
    if len(num) % 2 == 0:
        while num:
            front = num.pop(0)
            end = num.pop()
            if front != end:
                check = False
                break
    else:
        while len(num) > 1:
            front = num.pop(0)
            end = num.pop()
            if front != end:
                check = False
                break

    if check:
        answers.append("yes")
    else:
        answers.append("no")

for answer in answers:
    print(answer)
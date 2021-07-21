data = input()
word = input()

answer = []

for i in data:
    answer.append(i)

    if len(answer) >= len(word):
        queue = []
        count = 0
        check = True
        for j in range(-1, (-len(word))-1, -1):
            if answer[j] != word[j]:
                check = False
                break
        if check:
            num = 0
            while num<len(word):
                answer.pop()
                num += 1

if len(answer) == 0:

    print("FRULA")
else:
    print("".join(answer))
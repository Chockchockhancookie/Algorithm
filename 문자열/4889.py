answer = []
while True:
    data = input()
    num = 0
    if "-" in data:
        break
    queue = []
    for word in data:
        if not queue and word == "}":
            num += 1
            queue.append(word)
        elif queue and word == "}":
            queue.pop()
        else:
            queue.append(word)

    answer.append(num + len(queue)//2)
    print(queue)
for i in range(1, len(answer) + 1):
    print("{}. {}".format(i, answer[i - 1]))
#}{{}{{{}}{{{
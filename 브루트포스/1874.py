n = int(input())

queue = []
answer = []
count = 0
check = True
for _ in range(n):
    num = int(input())

    while count < num:
        count += 1
        queue.append(count)
        answer.append("+")

    if queue[-1] == num:
        queue.pop()
        answer.append("-")
    else:
        check = False
        break

if check:
    for i in answer:
        print(i)
else:
    print("NO")
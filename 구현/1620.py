n, m = map(int, input().split())

data = [input() for _ in range(n)]

answers = []
for _ in range(m):
    tmp = input()
    try:
        pocket = int(tmp)
    except:
        pocket = tmp
        answers.append(data.index(pocket)+1)
    else:
        answers.append(data[pocket-1])

for answer in answers:
    print(answer)
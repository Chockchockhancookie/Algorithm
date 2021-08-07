n = int(input())

data = []
for _ in range(n):
    word = input()
    data.append((len(word), word))

data = sorted(data, key=lambda x: (x[0], x[1]))

answer = []
for num, word in data:
    if word not in answer:
        answer.append(word)
        print(word)
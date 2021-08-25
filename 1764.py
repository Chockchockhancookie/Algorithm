import sys
input = sys.stdin.readline

n, m = map(int, input().split())

not_listen = {}
for _ in range(n):
    name = input().rstrip()
    not_listen[name] = 1

answers = []
for _ in range(m):
    name = input().rstrip()
    if name in not_listen:
        answers.append(name)

answers.sort()
print(len(answers))
for answer in answers:
    print(answer)
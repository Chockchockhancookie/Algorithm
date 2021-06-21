n = int(input())

before = []
for i in range(n):
    before.append(input())

after = []
for i in range(n):
    after.append(input())

count = 0
for i in range(n):
    tmp1 = before.index(before[i])
    tmp2 = after.index(before[i])


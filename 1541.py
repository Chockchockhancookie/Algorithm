import sys
input = sys.stdin.readline

data = input()
data = data.split('-')

num = []
for i in data:
    temp = list(map(int, i.split('+')))
    num.append(sum(temp))

count = num[0]
for i in num[1:]:
    count -= i

print(count)
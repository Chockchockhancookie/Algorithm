from itertools import permutations

n = int(input())
data = list(map(int, input().split()))

array = permutations(data)

answer = 0
for i in array:
    total = 0
    for a in range(len(i)-1):
        total += abs(i[a] - i[a+1])
    answer = max(answer, total)

print(answer)
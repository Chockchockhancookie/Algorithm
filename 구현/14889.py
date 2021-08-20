from itertools import combinations
import sys
input = sys.stdin.readline


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

people = [i for i in range(n)]

answer = sys.maxsize
for a in combinations(people, n//2):
    first = list(a)
    second = list(set(people) - set(first))

    first_sum, second_sum = 0, 0
    for i, j in combinations(first, 2):
        first_sum += data[i][j]+data[j][i]
    for i, j in combinations(second, 2):
        second_sum += data[i][j]+data[j][i]

    answer = min(answer, abs(first_sum-second_sum))

print(answer)
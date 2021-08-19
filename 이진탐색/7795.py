import sys
input = sys.stdin.readline


def find_number(num):
    left = 0
    right = m-1
    find = -1
    while left <= right:
        mid = (left+right)//2
        if end[mid] < num:
            left = mid+1
            find = mid
        else:
            right = mid-1
    return find


t = int(input())

answers = []
for _ in range(t):
    n, m = map(int, input().split())

    start = list(map(int, input().split()))
    start.sort()
    end = list(map(int, input().split()))
    end.sort()

    answer = 0
    for num in start:
        answer += (find_number(num)+1)

    answers.append(answer)

for answer in answers:
    print(answer)
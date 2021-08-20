import sys
input = sys.stdin.readline

n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())


answer = n
for num in rooms:
    num -= b

    if num <= 0:
        continue

    if num % c == 0:
        answer += (num//c)
    else:
        answer += (num//c)+1

print(answer)
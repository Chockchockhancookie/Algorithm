import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
array = list(sorted(set(data)))     # set으로 중복제거, 정렬

dic = {array[i]: i for i in range(len(array))}   # dict으로 좌표 값을 key로 index를 value로

for i in data:
    print(dic[i], end=" ")
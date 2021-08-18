import sys
input = sys.stdin.readline

arr = {}

n = int(input())
find_data = list(map(int, input().split()))
for i in find_data:
    arr[i] = 1

m = int(input())
data = list(map(int, input().split()))
for a in data:
    if a not in arr:
        print(0)
    else:
        print(1)
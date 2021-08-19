import sys
input = sys.stdin.readline


def find_number(x):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if data[mid] < x:
            start = mid+1
        elif data[mid] > x:
            end = mid-1
        else:
            return 1
    return 0


t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    m = int(input())
    find = list(map(int, input().split()))

    for num in find:
        print(find_number(num))
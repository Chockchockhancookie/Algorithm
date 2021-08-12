import math
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
num = math.floor((y/x) * 100)

start, end = 0, 1000000000
while start <= end:
    mid = (start+end)//2
    nx, ny = x + mid, y + mid
    if num < math.floor((ny/nx)*100):
        end = mid-1
    else:
        start = mid+1

print(end+1)
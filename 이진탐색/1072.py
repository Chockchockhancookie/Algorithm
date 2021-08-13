import math
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
num = math.floor(y*100/x)

start, end = 0, 1000000000
if num >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start+end)//2
        nx, ny = x + mid, y + mid
        if num < math.floor(ny*100//nx):
            end = mid-1
        else:
            start = mid+1
    print(end+1)
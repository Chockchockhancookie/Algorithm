import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

arr = []
for i in range(n):
    if data[i] == 1:
        arr.append(i)

start, end = 0, k-1
if len(arr) < k:
    print(-1)
    sys.exit()

answer = sys.maxsize
while True:
    tmp = arr[end] - arr[start] + 1
    answer = min(answer, tmp)
    if end == len(arr)-1:
        break
    start += 1
    end += 1

print(answer)
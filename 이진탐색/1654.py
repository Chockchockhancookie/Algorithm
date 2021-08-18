import sys
input = sys.stdin.readline

k, n = map(int, input().split())    # 가지고 있는 랜선의 수, 필요한 랜선의 수
data = [int(input()) for _ in range(k)]

start, end = 1, max(data)+1
answer = 0
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for l in data:
        cnt += l // mid

    if cnt < n:
        end = mid-1
    else:
        start = mid+1
        answer = max(answer, mid)

print(answer)
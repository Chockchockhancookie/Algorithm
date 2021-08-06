def find_money():
    money = 0
    num = 0
    for data in datas:
        if mid < data:
            return m+1
        if money >= data:
            money -= data
        else:
            money = mid - data
            num += 1
    return num


n, m = map(int, input().split())
datas = [int(input()) for _ in range(n)]

answer = int(1e9)

start, end = 0, int(1e9)
while start <= end:
    mid = (start+end) // 2
    tmp = find_money()
    if tmp > m:
        start = mid+1
    else:
        answer = min(answer, mid)
        end = mid-1

print(answer)
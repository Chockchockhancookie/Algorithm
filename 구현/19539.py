# 1 - 총합을 3으로 나눴을 때 0 이 아니면 "NO"
# 2 - 각각의 나무에 2를 나눴을 때 몫의 합은 물을 주는데 최대로 필요한 횟수
# 2가 1보다 작으면 "NO" 아니면 "YES"
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

sum_value = sum(data)
up = sum_value // 3
down = sum_value % 3

if down != 0:
    print("NO")
else:
    for i in data:
        up -= i//2

    if up <= 0:
        print("YES")
    else:
        print("NO")
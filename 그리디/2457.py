import sys
input = sys.stdin.readline
month_day = {
    1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
    7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334
}


def change_date(m, d):
    return month_day[m]+d


n = int(input())

flowers = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    flowers.append([change_date(a, b), change_date(c, d)])

flowers = sorted(flowers, key=lambda x: (x[0], x[1]))

start, end = 0, 60                  # 1월~3월
start_date, end_date = 60, 334      # 3월~12월

x = -1
change = 0
tmp = 0
stack = []

while end <= end_date and x < n:
    change = 0
    x += 1
    for i in range(x, n):
        if flowers[i][0] > end:
            break
        if tmp < flowers[i][1]:
            tmp = flowers[i][1]
            x = i
            change = 1
    if change == 1:
        end = tmp
        stack.append(flowers[x])
    else:
        stack = []
        break
print(len(stack))
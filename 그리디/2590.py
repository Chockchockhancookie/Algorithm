import sys
input = sys.stdin.readline

a = [0]
now = 0

for _ in range(6):
    a.append(int(input()))

cnt = a[6]
a[6] = 0

cnt += a[5]
a[1] -= 11 * a[5]

if a[1] < 0:
    a[1] = 0

cnt += a[4]
now = 20 * a[4]

if 4 * a[2] >= now:
    a[2] -= now // 4
    now %= 4
else:
    now -= 4 * a[2]
    a[2] = 0

a[1] -= now

if a[1] < 0:
    a[1] = 0

cnt += a[3] // 4
a[3] %= 4

if a[3] == 3:
    cnt += 1
    if a[2] > 0:
        a[2] -= 1
        a[1] -= 5
    else:
        a[1] -= 9

elif a[3] == 2:
    cnt += 1
    if a[2] >= 3:
        a[2] -= 3
        a[1] -= 6
    elif a[2] == 2:
        a[2] = 0
        a[1] -= 10
    elif a[2] == 1:
        a[2] = 0
        a[1] -= 14
    else:
        a[1] -= 18

elif a[3] == 1:
    cnt += 1
    if a[2] >= 5:
        a[2] -= 5
        a[1] -= 7
    elif a[2] == 4:
        a[2] = 0
        a[1] -= 11
    elif a[2] == 3:
        a[2] = 0
        a[1] -= 15
    elif a[2] == 2:
        a[2] = 0
        a[1] -= 19
    elif a[2] == 1:
        a[2] = 0
        a[1] -= 23
    else:
        a[1] -= 27

cnt += a[2] // 9
a[2] %= 9

if a[2] == 8:
    cnt += 1
    a[1] -= 4
elif a[2] == 7:
    cnt += 1
    a[1] -= 8
elif a[2] == 6:
    cnt += 1
    a[1] -= 12
elif a[2] == 5:
    cnt += 1
    a[1] -= 16
elif a[2] == 4:
    cnt += 1
    a[1] -= 20
elif a[2] == 3:
    cnt += 1
    a[1] -= 24
elif a[2] == 2:
    cnt += 1
    a[1] -= 28
elif a[2] == 1:
    cnt += 1
    a[1] -= 32

if a[1] < 0:
    a[1] = 0

cnt += a[1] // 36

if a[1] % 36 > 0:
    cnt += 1

print(cnt)
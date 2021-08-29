import math

n, m = map(int, input().split())

data = [True] * (m+1)
data[1] = False

for i in range(2, int(math.sqrt(m))+1):
    if data[i]:
        j = 2
        while i * j <= m:
            data[i*j] = False
            j += 1

for a in range(n, m+1):
    if data[a]:
        print(a)
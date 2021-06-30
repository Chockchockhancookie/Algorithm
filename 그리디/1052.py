n, k = map(int, input().split())
z = n
while bin(n).count('1')>k:
    n += (n & -n)
print(n - z)
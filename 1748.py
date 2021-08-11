import sys
input = sys.stdin.readline

n = int(input())
num = len(str(n))

count = 0

for i in range(num-1):
    count += 9 * 10 ** i * (i+1)

print(count + (n - 10 ** (num-1) +1) * num)
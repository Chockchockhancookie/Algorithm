import sys
input = sys.stdin.readline

n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]

flowers = sorted(flowers, key=lambda x: (x[0], x[1], -x[2], -x[3]))
print(flowers)
count = 0

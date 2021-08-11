n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

for a in range(n):
    for b in range(m):
        print(data[a][b], end=" ")
    print()
print()

array = data[:]
for a in range(n):
    for b in range(m):
        print(array[a][b], end=" ")
    print()

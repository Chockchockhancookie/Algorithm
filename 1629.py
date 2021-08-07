def find(x):
    if x == 1:
        return a % c
    if x % 2 == 0:
        tmp = find(x//2)
        return tmp*tmp%c
    else:
        tmp = find(x//2)
        return tmp*tmp*a%c


a, b, c = map(int, input().split())
print(find(b))
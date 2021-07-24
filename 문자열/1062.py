n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(input()))

if k < 5:
    print(0)
else:
    alpha = [0] * 26
    basic = ['a', 'n', 't', 'i', 'c']
    for i in basic:
        alpha[ord(i) - ord('a')] = 1
    num = 5

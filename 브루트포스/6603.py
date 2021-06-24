from itertools import combinations

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break

    del data[0]

    result = list(combinations(data, 6))
    for i in result:
        for a in i:
            print(a, end=' ')
        print()
    print()

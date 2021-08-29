import sys
input = sys.stdin.readline


def find_number(x, y, n):
    global minus_one, zero, plus_one
    number = graph[x][y]

    for a in range(x, x+n):
        for b in range(y, y+n):
            if graph[a][b] != number:
                find_number(x, y, n // 3)
                find_number(x, y + n // 3, n // 3)
                find_number(x, y + 2 * n // 3, n // 3)
                find_number(x + n // 3, y, n // 3)
                find_number(x + n // 3, y + n // 3, n // 3)
                find_number(x + n // 3, y + 2 * n // 3, n // 3)
                find_number(x + 2 * n // 3, y, n // 3)
                find_number(x + 2 * n // 3, y + n // 3, n // 3)
                find_number(x + 2 * n // 3, y + 2 * n // 3, n // 3)
                return

    if number == -1:
        minus_one += 1
        return
    elif number == 0:
        zero += 1
        return
    else:
        plus_one += 1
        return


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

minus_one, zero, plus_one = 0, 0, 0
find_number(0, 0, n)

print(minus_one)
print(zero)
print(plus_one)
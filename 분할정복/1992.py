import sys
input = sys.stdin.readline


def find_number(x, y, n):
    global zero, one
    number = graph[x][y]
    for a in range(x, x+n):
        for b in range(y, y+n):
            if graph[a][b] != number:
                print("(", end="")
                find_number(x, y, n//2)
                find_number(x, y+n//2, n//2)
                find_number(x+n//2, y, n//2)
                find_number(x+n//2, y+n//2, n//2)
                print(")", end="")
                return

    print(number, end="")
    return


n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

zero, one = 0, 0
find_number(0, 0, n)
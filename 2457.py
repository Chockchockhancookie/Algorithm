import sys
input = sys.stdin.readline


def flower():
    count = 0
    start_day = [0, 0]
    end_day = [0, 0]
    check_day = []

    for i in range(n):
        for j in range(n):
            if flowers[j][0] < start_day


n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]

flowers = sorted(flowers, key=lambda x: (x[0], x[1], -x[2], -x[3]))

print(flower())
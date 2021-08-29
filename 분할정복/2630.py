import sys
input = sys.stdin.readline


def find_paper(x, y, n):
    global blue, white
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                find_paper(x, y, n//2)              # 1사분면
                find_paper(x, y+n//2, n//2)         # 2사분면
                find_paper(x+n//2, y, n//2)         # 3사분면
                find_paper(x+n//2, y+n//2, n//2)    # 4사분면
                return

    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return


n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

blue, white = 0, 0
find_paper(0, 0, n)
print(white)
print(blue)
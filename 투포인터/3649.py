import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000    # 구멍의 너비
        n = int(input())    # 레고 조각의 수
        data = [int(input()) for _ in range(n)]
        data.sort()

        check = False
        start, end = 0, n-1
        while start < end:
            tmp = data[end] + data[start]
            if tmp == x:
                print("yes", data[start], data[end])
                check = True
                break
            elif tmp < x:
                start += 1
            else:
                end -= 1

        if not check:
            print("danger")

    except:
        break
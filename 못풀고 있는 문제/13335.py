import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())    # 트럭의 수, 다리길이, 최대하중
trucks = list(map(int, input().split()))
data = [0] * w

w = 0
start, end = 0, 0
time = 0
while True:
    time += 1
        if w+trucks[end] <= weight:
            w += trucks[end]]
            end += 1

        for i in range(start, end):
            l[i] += 1
            if l[start] > length:
                w -= trucks[start
                start += 1

    print(l)
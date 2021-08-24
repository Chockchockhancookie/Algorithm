import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())   # 다리를 건너는 트럭의 수, 다리의 길이, 최대하중

data = list(map(int, input().split()))

weight, start = 0, 0
while start <= n:
    now = data[start]
    if weight+now < l
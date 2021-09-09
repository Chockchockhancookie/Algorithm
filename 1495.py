import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
data = list(map(int, input()))

dp = [s] * (n+1)
import sys
input = sys.stdin.readline

t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    data = [0] + list(map(int, input().split()))
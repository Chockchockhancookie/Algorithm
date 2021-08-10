import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(input().rstrip())

answer = 0
for i in range(n):
    if data[i] == "P":
        for a in range(i-k, i+k+1):
            if 0 <= a < n and data[a] == "H":
                answer += 1
                data[a] = ""
                break

print(answer)
import sys
input = sys.stdin.readline

n = int(input())
s = int(input())
data = list(input())

p = ["I"] + ["O", "I"] * n

answer = 0
for i in range(s-len(p)+1):
    if data[i] == "I":
        tmp = data[i:i+len(p)]
        check = True
        for j in range(len(p)):
            if tmp[j] != p[j]:
                check = False
        if check:
            answer += 1

print(answer)
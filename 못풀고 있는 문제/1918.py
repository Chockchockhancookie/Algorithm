import sys
input = sys.stdin.readline

data = input().rstrip()

stack = []
answer = ""
for txt in data:
    if txt.isalpha():
        answer += txt
    else:
        if txt == "(":
            stack.append(txt)
        elif x ==

print(answer)
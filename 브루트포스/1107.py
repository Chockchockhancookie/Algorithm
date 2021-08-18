n = int(input())
m = int(input())
if m:
    wrong = list(map(int, input().split()))
else:
    wrong = list()

answer = abs(100-n)
for num in range(1000001):
    for i in str(num):
        if int(i) in wrong:
            break
    else:
        answer = min(answer, len(str(num)) + abs(num - n))

print(answer)
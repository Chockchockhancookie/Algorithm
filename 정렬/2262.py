n = int(input())
data = list(map(int, input().split()))

answer = 0
for i in range(n-1):
    target = max(data)
    target_idx = data.index(target)
    if target_idx == 0:
        answer += target - data[1]
    elif target_idx == len(data) - 1:
        answer += target - data[-2]
    else:
        answer = min(answer + target - data[target_idx - 1], answer + target - data[target_idx + 1])

    del data[target_idx]

print(answer)
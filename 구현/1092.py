n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)

count = 0
check = [0] * m
position = [0] * n
time = 0

if max(box) > max(crain):
    print(-1)
else:
    while count < m:
        for i in range(n):
            while position[i] < m:
                if not check[position[i]] and crain[i] >= box[position[i]]:
                    check[position[i]] = True
                    position[i] += 1
                    count += 1
                    break
                position[i] += 1
        time += 1
    print(time)
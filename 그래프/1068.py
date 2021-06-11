from collections import deque

# 78%에서 틀림
def find_node(start):
    count = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now == purpose:
            continue
        if len(tree[now]) == 0:
            count += 1
        else:
            num = len(tree[now])
            for i in tree[now]:
                if i == purpose and num-1 == 0:
                    count += 1
                queue.append(i)
    return count


n = int(input())

tree = [[] for _ in range(n)]
top = 0
data = list(map(int, input().split()))
for i in range(len(data)):
    if data[i] == -1:
        top = i
    else:
        tree[data[i]].append(i)

purpose = int(input())
answer = find_node(top)

print(answer)
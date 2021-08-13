from collections import deque

a, b = map(int, input().split())
MAX = 10000
counts = [0] * (MAX + 1)


def sosoo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


counts[a] = 0
q = deque()
q.append(a)
while q:
    x = q.popleft()
    if x == b: break

    for i in range(4):
        A = list(map(int, str(x)))
        for j in range(1, 10):
            if A[i] == j: continue
            A[i] = j
            B = (A[0] * 1000) + (A[1] * 100) + (A[2] * 10) + A[3]
            if 1000 < B < MAX and sosoo(B) and not counts[B]:
                counts[B] = counts[x] + 1
                q.append(B)
print(counts[b])

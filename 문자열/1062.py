import sys
input = sys.stdin.readline


def bfs(idx, count):
    global answer
    if count == k-5:
        num = 0
        for words in data:
            for word in words:
                if alpha[ord(word)-ord('a')] != 1:
                    break
            else:
                num += 1
        answer = max(answer, num)
        return

    for i in range(idx, 26):
        if alpha[i] == 0:
            alpha[i] = 1
            bfs(i, count+1)
            alpha[i] = 0


n, k = map(int, input().rstrip().split())
data = []

alpha = [0] * 26
basic = ['a', 'n', 't', 'i', 'c']
for i in basic:
    alpha[ord(i) - ord('a')] = 1

for _ in range(n):
    data.append(list(input().rstrip())[4:-4])

remain = []

if k < 5:
    print(0)
else:
    answer = 0
    bfs(0, 0)

    print(answer)
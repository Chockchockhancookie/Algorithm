def dfs(x, count):
    global answer
    if count == k - 5:
        read_count = 0
        for word in data:
            for a in word:
                if not alpha[ord(a) - ord("a")]:
                    break
            else:
                read_count += 1
        answer = max(answer, read_count) if answer else read_count
        return

    for i in range(x, 26):
        if not alpha[i]:
            alpha[i] = True
            dfs(i, count + 1)
            alpha[i] = False


n, k = map(int, input().split())
if k < 5:
    print(0)
    exit()

data = [set(input()) for _ in range(n)]
alpha = [False] * 26
for i in ["a", "c", "i", "t", "n"]:
    alpha[ord(i) - ord("a")] = True

answer = None
dfs(0, 0)
print(answer)
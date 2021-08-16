import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(x, data, idx, visited, stack):
    global num
    idx[x] = num
    data[x] = num
    num += 1
    visited[x] = True
    stack.append(x)
    for node in edges[x]:
        if idx[node] == -1:
            dfs(node, data, idx, visited, stack)
            data[x] = min(data[x], data[node])
        elif visited[node]:
            data[x] = min(data[x], idx[node])

    tmp = -1
    scc = []
    if data[x] == idx[x]:
        while tmp != x:
            tmp = stack.pop()
            scc.append(tmp)
            visited[tmp] = -1
        result.append(sorted(scc))


t = int(input())

answers = []
for _ in range(t):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        indegree[b] += 1

    count = 0
    num = 0
    stack = []
    result = []
    data = [-1] * (n+1)
    idx = [-1] * (n+1)
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if idx[i] == -1:
            dfs(i, data, idx, visited, stack)

    for scc in result:
        if len(scc) == 1:
            if indegree[scc[0]] == 0:
                count += 1
        else:
            check = True
            for j in scc:
                if indegree[j] > 1:
                    check = False
            if check:
                count += 1
    print(count)
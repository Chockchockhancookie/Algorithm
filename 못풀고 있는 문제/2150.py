import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(start, visited, stack):
    visited[start] = True
    for node in edges[start]:
        if not visited[node]:
            stack.append(node)
            dfs(node, visited, stack)
    stack.append(start)


def reverseGraph():
    reverse_graph = [[] for _ in range(v+1)]
    for i in range(1, v+1):
        for j in edges[i]:
            reverse_graph[j].append(i)
    return reverse_graph


def reverseDfs(v, visited, stack):
    visited[v] = True
    stack.append(v)
    for w in reverse_graph[v]:
        if not visited[w]:
            reverseDfs(w, visited, stack)


v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    edges[a].append(b)

visited = [False] * (v+1)

stack = []
for i in range(1, v+1):
    if not visited[i]:
        dfs(i, visited, stack)

reverse_graph = reverseGraph()

visited = [False] * (v+1)
results = []

while stack:
    ssc = []
    now = stack.pop()
    if not visited[now]:
        reverseDfs(now, visited, ssc)
        results.append(sorted(ssc))

results.sort()
print(len(results))
for data in results:
    for i in range(len(data)+1):
        if i == len(data):
            print(-1)
        else:
            print(data[i], end=" ")
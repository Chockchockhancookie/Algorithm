import sys
input = sys.stdin.readline

n, m = map(int, input().split())

not_listen = set(list(input().rstrip() for _ in range(n)))
not_look = set(list(input().rstrip() for _ in range(m)))

sum_data = list(not_look & not_listen)
sum_data.sort()
print(len(sum_data))
for txt in sum_data:
    print(txt)
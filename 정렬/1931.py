import sys
input = sys.stdin.readline

n = int(input())
time_table = []

for _ in range(n):
    s, e = map(int, input().split())
    time_table.append([s, e])

table = [[0, 1]]

time_table.sort(key=lambda x: (x[1], x[0], -x[3]))

count = 1
end_time = time_table[0][1]
for i in range(1, n):
    if time_table[i][0] >= end_time:
        count += 1
        end_time = time_table[i][1]

print(count)
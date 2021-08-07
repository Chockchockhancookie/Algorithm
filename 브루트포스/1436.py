# n번째로 작은 종말번호 찾기!
n = int(input())

check_num = 666
count = 0
while True:
    if '666' in str(check_num):
        count += 1
    if count == n:
        print(check_num)
        break
    check_num += 1
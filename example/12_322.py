data = input()

al = []
total = 0

for i in data:
    if i.isalpha():
        al.append(i)
    else:
        total += int(i)

al.sort()

if total != 0:
    al.append(str(total))
print("".join(al))
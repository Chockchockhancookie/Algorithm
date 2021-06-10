n = int(input())

data = []
for _ in range(n):
     data.append(input())

dict = {}
for word in data:
    num = len(word)-1
    for i in word:
        if i in dict:
            dict[i] += pow(10, num)
        else:
            dict[i] = pow(10, num)
        num -= 1

array = []
for value in dict.values():
    array.append(value)

array.sort(reverse=True)

result, a = 0, 9

for i in range(len(array)):
    result += array[i] * a
    a -= 1

print(result)
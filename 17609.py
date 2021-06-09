def find_rotation(arr, left, right):
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            first = delete_word(arr, left + 1, right)
            second = delete_word(arr, left, right - 1)
            if first or second:
                return 1
            else:
                return 2
    return 0


def delete_word(arr, left, right):
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


n = int(input())

answer = []
for _ in range(n):
    arr = list(input())
    left, right = 0, len(arr)-1
    final = find_rotation(arr, left, right)
    answer.append(final)

for i in range(n):
    print(answer[i])
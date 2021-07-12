def productExceptSelf(nums):
    answer = []
    print(nums)
    for i in range(len(nums)):
        left, right = i - 1, i + 1
        tmp = 1
        print(left, right)
        while left >= 0:
            print(0)
            tmp *= nums[left]
            left -= 1
        while right < len(nums):
            print(1)
            tmp *= nums[right]
            right += 1
        answer.append(tmp)
    return answer


print(productExceptSelf([1, 2, 3, 4]))
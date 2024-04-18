def concateArr(nums):
    n = len(nums)
    for i in range(n):
        nums.append(nums[i])
    return nums

print(concateArr([1,3,4,2,1]))
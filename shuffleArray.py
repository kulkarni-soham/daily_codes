def shuffleArray(nums, n):
    ans = []
    mid = len(nums)//2
    for i in range(mid):
        ans.append(nums[i])
        ans.append(nums[i+mid])
    return ans

ans = shuffleArray([1,2,5,23,8,27],3)
print(ans)
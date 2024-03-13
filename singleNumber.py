def singleOccur(nums):
    for i in nums:
        if(nums.count(i)==1):
            return i
        
    return -1

print(singleOccur([1,0,0, 1,2,3,4,3,3,2]))
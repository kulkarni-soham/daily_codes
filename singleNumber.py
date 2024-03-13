def singleOccur(nums):
    d = {}
    res = 0
    for i in nums:
        if (i not in d):
            d[i] = 1
        else:
            d[i] += 1
            
    for k,v in d.items():
        if (v == 1):
            res = k
            
    return res
print(singleOccur([1,0,0,1,2,3,4,3,3,2]))
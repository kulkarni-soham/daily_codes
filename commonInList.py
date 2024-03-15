def intersection(nums1, nums2):
    l1 = []
    for i in nums1:
        if i in nums2:
            if i not in l1:
                l1.append(i)
                
    return l1

print(intersection([1,2,2,1],[2,2]))
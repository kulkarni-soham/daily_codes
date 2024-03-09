from collections import Counter
def relativeSortArray( arr1, arr2) :
    nums = set(arr2)
    nums1 = []
    nums2 = []
    for i in arr1:
        if i in nums : nums1.append(i)
        else: nums2.append(i)
    d = Counter(nums1)
    ans = []
    for i in arr2:
        ans += [i] * d[i]

    return ans + sorted(nums2)

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1, arr2))
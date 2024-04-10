class Solution:
    def merge(self, nums1, m: int, nums2, n: int) :

        for i in range(0, len(nums2)):
            nums1[m] = nums2[i]
            m+=1 
        nums1 = sorted(nums1)
        print(nums1)
        return sorted(nums1)
    
print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))
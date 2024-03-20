class Solution:
    def search(self, nums, target):
        return target in set(nums)
    
obj = Solution()
print(obj.search([2,5,6,0,0,1,2], 0))
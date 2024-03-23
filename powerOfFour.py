import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if math.log(n, 4).is_integer() == True:
            return True
        return False
    
obj = Solution()
print(obj.isPowerOfFour(64))
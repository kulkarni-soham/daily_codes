class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = ''
        for i in s:
            if ord(i)<123 and ord(i)>96:
                a = a + i

        left = 0
        right = len(a)-1
        while left<right:
            if a[left] != a[right]:
                return False

        return True
    

class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in (')', '}', ']'):
            return False

        stack = []

        par = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for paran in s:
            if paran in ('(', '[', '{'): # 1
                stack.append(paran)

            elif stack and par[paran] == stack[-1]: # 2
                stack.pop()

            else:
                return False # 3

        return len(stack) == 0
    
print(Solution().isValid('{()}[]'))
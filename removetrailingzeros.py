# num="51230100"
# l=[]
# for i in num:
#     l.append(i)
# print(l)
    
# for i in range(len(l)):
#     if l[-1]=="0":
#         l.remove(l[-1])
# print(l)

# str=''.join(l[::1])
# print(str)

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        number = int(num)
        while number%10 == 0:
            number = number//10
        num = ''.join(str(number));
        
        return num
    
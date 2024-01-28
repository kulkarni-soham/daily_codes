import math
def reverse(x):
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31
    reverse = 0
    while x != 0:
        if(x>MAX_INT or x<MIN_INT):
            return 0
        digit = x%10 if x > 0 else x % -10
        
        reverse = reverse * 10 + digit
        x = math.trunc(x/10)
        
    return reverse

print(reverse(-1))
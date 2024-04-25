def tribonacci(n):
    a = 0
    b = 1
    c = 1
    result = 0
    if n == 0:
        return 0
    elif n < 3 :
        return 1
    for i in range(n-2):
        result = a + b + c
        a = b
        b = c
        c = result
        
    return result

print(tribonacci(5))
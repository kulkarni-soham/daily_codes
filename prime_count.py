def primeCount(n):
    num = 1
    prime = [2]
    if n==2 :
        return 1, prime
    
    if n == 0 or n == 1:
        return 0, None
    
    for i in range (3,n+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            num += 1
            prime.append(i)
            
    return num, prime

user_input = int(input("Input number : "))
count, num = primeCount(user_input)
if count > 1:
    print(f"There are {count} prime numbers less than {user_input} , they are ", end = "")
    for i in range(len(num)):
        if i == len(num)-1:
            print(num[i], end="\n")
        
        else:
            print(num[i], end=", ")

elif count == 1:
    print(f"There is {count} prime number less than equal to {user_input}, it is {num}")
    
    
else:
    print(count)
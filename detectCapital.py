def detectCapital(word)->bool:
    allCaps = True
    for i in word:
        if ord(i)<=90:
            allCaps = True
        else:
            allCaps = False
            break
        
    if allCaps == True:
        return True
    
    for i in range(1,len(word)):
        if ord(word[i])<97:
            return False
        
    return True 

print(detectCapital("NexaByte"))
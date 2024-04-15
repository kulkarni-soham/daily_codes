def isPalidrome(str, start, end, flag):
    if flag == False:
        return False
    if start == end or start > end:
        flag = True
        return True
    if str[start] == str[end]:
        flag = True
    else:
        flag = False
        return False
    
    return isPalidrome(str, start+1, end-1, flag)
    
str = 'racecr'
print(isPalidrome(str, 0, len(str)-1, True))
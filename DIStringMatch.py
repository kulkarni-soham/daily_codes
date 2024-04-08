def diStringMatch(s) :
    lp = 0
    rp = len(s)
    result = []
    for i in range(len(s)):
        if s[i] == 'I':
            result.append(lp)
            lp+=1
        else :
            result.append(rp)
            rp-=1
    if s[-1] == 'I':
        result.append(rp)
    else:
        result.append(lp)
    
    return result

print(diStringMatch('DIDI'))
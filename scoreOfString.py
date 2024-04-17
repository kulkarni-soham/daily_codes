def scoreOfString(s) :
    result = 0
    for i in range(0,len(s)-1) :
        if ord(s[i])>ord(s[i+1]) :
            r1 = ord(s[i]) - ord(s[i+1])
        else:
            r1 = ord(s[i+1]) - ord(s[i])
        result += r1

    return result

print(scoreOfString("soham"))
def toLowerCase( s) :
    low = ""
    for i in s:
        if i.isupper():
            low += i.lower()
        else:
            low+=i
    return low

print(toLowerCase("Hello"))
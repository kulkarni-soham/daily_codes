
def reverseVowels(s) :
    start = 0
    end = len(s) - 1
    sa = list(s)
    l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while(start < end):
        if ((sa[start] in l) and (sa[end] in l)):
            temp = sa[start]
            sa[start] = sa[end]
            sa[end] = temp
            start += 1
            end -= 1

        elif ((sa[start] in l) and (sa[end] not in l)):
            end -= 1 

        elif ((sa[start] not in l) and (sa[end] in l)):
            start += 1

        else:
            start += 1
            end -= 1
    result = ''.join(sa)
    s = result
    return s

print(reverseVowels('hello'))
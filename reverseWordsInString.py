def reverse(s):
    li = s.split()
    newList = []
    for i in li:
        newList.append(i[::-1])
    str = ' '.join(newList)
    return str

print(reverse('hello python its soham'))
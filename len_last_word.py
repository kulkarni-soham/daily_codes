def lenLastWord(s):
    return len(s.split()[len(s.split())-1])

print(lenLastWord("hello  world "))
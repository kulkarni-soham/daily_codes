def validAnagram(s, t):
    return sorted(s) == sorted(t)

print(validAnagram('anagram', 'nagaram'))
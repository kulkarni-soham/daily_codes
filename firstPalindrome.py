def firstPalindrome(words):
    for i in words:
        if i == i[::-1]:
            return i
    return ''

print(firstPalindrome(["palindrome", "racecar", "hello"]))
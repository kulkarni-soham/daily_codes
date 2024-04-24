def truncateSentence(s, k):
    l = s.split()
    return " ".join(l[:k])
print(truncateSentence("This is python code", 3))
def Counter(arr):
    s = {}
    for i in arr:
        s[i] = (arr.count(i))
        
    return s

def uniqueOccurences(arr):
    occurrencesMap = Counter(arr)
    uniqueCountsSet = set()

    for i in occurrencesMap.values():
        if i in uniqueCountsSet:
            return False
        uniqueCountsSet.add(i)

    return True

print(uniqueOccurences([1,2,2,1,1,3]))
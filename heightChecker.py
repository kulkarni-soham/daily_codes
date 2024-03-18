class HeightChecker:
    def heightChecker(self, heights):
        count = 0
        self.expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != self.expected[i]:
                count += 1
                
        return count
obj = HeightChecker()
print(obj.heightChecker([1,2,3,1,4]))
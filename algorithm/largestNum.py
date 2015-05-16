class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        numStr = map(str, nums)
        numStr.sort(cmp=self.compare, reverse=True)
        return str(int(''.join(numStr)))
    
    def compare(self, s1, s2):
        if s1 == s2: return 0
        lenS1, lenS2 = len(s1), len(s2)
        for i in xrange(min(lenS1, lenS2)):
            if s1[i] < s2[i]: return -1
            if s1[i] > s2[i]: return 1
        return self.compare(s1, s2[lenS1:]) if lenS1 < lenS2 \
        else self.compare(s1[lenS2:], s2)


sol = Solution()
print sol.largestNumber([128, 12])
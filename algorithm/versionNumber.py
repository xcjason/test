class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        if v1 == v2: return 0
        lenV1, lenV2 = len(v1), len(v2)
        for i in xrange(min(lenV1, lenV2)):
            if v1[i] > v2[i]: return 1
            if v1[i] < v2[i]: return -1
        if lenV1 > lenV2:
            if sum(v1[lenV2:]) == 0: return 0
            else: return 1
        if lenV1 < lenV2:
            if sum(v2[lenV1:]) == 0: return 0
            else: return -1


sol = Solution()
print sol.compareVersion('1', '1.0')
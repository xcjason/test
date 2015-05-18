class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}    
    def multiply_slow(self, num1, num2):
        l1 = [int(i) for i in list(num1)]
        l2 = [int(i) for i in list(num2)]
        
        len1, len2 = len(l1), len(l2)
        res = [0] * (len1 + len2)
        for i in xrange(len1):
            for j in xrange(len2):
                tmp = [l1[i] * l2[j]] + [0] * (len1 - i + len2 - j - 2)
                for k in xrange(1, len(tmp) + 1):
                    res[-k] = res[-k] + tmp[-k]
        for i in xrange(1, len(res)):
            res[-i - 1] += res[-i] / 10
            res[-i] %= 10
        return ''.join(map(str, res)).lstrip('0')

    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0': return '0'
        l1 = [int(i) for i in list(num1)]
        l2 = [int(i) for i in list(num2)]
        len1, len2 = len(l1), len(l2)
        res = [0] * (len1 + len2)
        for i in xrange(len1):
            tmp = [l1[i] * n for n in l2] + [0] * (len1 - i - 1)
            for k in xrange(1, len(tmp) + 1):
                res[-k] = res[-k] + tmp[-k]
        for i in xrange(1, len(res)):
            res[-i - 1] += res[-i] / 10
            res[-i] %= 10
        return ''.join(map(str, res)).lstrip('0')

sol = Solution()
print sol.multiply('67', '23')
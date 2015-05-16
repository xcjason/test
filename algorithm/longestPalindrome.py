class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        lenS = len(s)
        res = ''
        if lenS <= 2: return s
        for i in xrange(1, lenS - 1):
            length = 0
            tmp = ''
            while length <= min(i, lenS - i - 1):
                if s[i - length] == s[i + length]: 
                    tmp = s[i - length: i + length + 1]
                    length += 1
                    continue
                else: break
            if len(tmp) > len(res): res = tmp
            length = 0
            while length <= min(i, lenS - i - 2):
                if s[i - length] == s[i + length + 1]: 
                    tmp = s[i - length: i + length + 2]
                    length += 1
                    continue
                else: break
            if len(tmp) > len(res): res = tmp
        return res

    def longestPalindrome_2(self, s):
        lenS = len(s)
        finalS, finalE = 0, 0
        for i in xrange(2 * lenS):
            start = i / 2
            end = start + i % 2
            tmpS, tmpE = 0, 0
            while start >= 0 and end < lenS and s[start] == s[end]:
                tmpS, tmpE = start, end
                start -= 1; end += 1
            if tmpE - tmpS > finalE - finalS: finalS, finalE = tmpS, tmpE
        return s[finalS: finalE + 1]

if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindrome('cc')
    print sol.longestPalindrome('ccc')
    print sol.longestPalindrome('aaaa')
    print sol.longestPalindrome('bcc')
    print sol.longestPalindrome('aaabd')
    print sol.longestPalindrome('daabbaa')
    print sol.longestPalindrome('abb')
    print '============================='
    print sol.longestPalindrome_2('ccc')
    print sol.longestPalindrome_2('aaaa')
    print sol.longestPalindrome_2('bcc')
    print sol.longestPalindrome_2('aaabd')
    print sol.longestPalindrome_2('abb')

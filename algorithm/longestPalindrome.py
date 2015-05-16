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

if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindrome('cc')
    print sol.longestPalindrome('ccc')
    print sol.longestPalindrome('aaaa')
    print sol.longestPalindrome('bcc')
    print sol.longestPalindrome('aaabd')
    print sol.longestPalindrome('daabbaa')

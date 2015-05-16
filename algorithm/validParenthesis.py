class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = ['#']
        res, tmp = 0, 0
        for i in s:
            if stack[-1] == '(' and i == ')':
                tmp += 2
                stack.pop()
            else:
                if tmp > res: res = tmp
                tmp = 0
                stack.append(i)
        return max(res, tmp)

if __name__ == '__main__':
    sol = Solution()
    print sol.longestValidParentheses('()()')

# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

22: Generate Parentheses
https://oj.leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"

===Comments by Dabay===
递归。
用left和right来记录剩余的左右括号数量。
如果都不剩余了，把结果放入要返回的列表中。
如果剩下的左括号比右括号多，说明不是合法的组合，返回。
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        def generateParenthesis2(left, right, string, res):
            if left == 0 and right == 0:
                res.append(string)
                return
            if left > right:
                return
            if left > 0:
                generateParenthesis2(left-1, right, string + "(", res)
            if right > 0:
                generateParenthesis2(left, right-1, string + ")", res)

        res = []
        generateParenthesis2(n, n, "", res)
        return res


def main():
    sol = Solution()
    print sol.generateParenthesis(4)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

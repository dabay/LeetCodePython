# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

===Comments by Dabay===
用一个stack来记录左括号'（'的位置；
start来记录这个左括号之前自封闭的位置。也就是说，实际上匹配到这个左括号的时候，计算右括号到start的长度。

当遇到右括号'('的时候，
    把i和start中小的那个数入栈；同时，start更新指向i的下一个位置。
当遇到左括号')'的时候，
    如果stack不为空，
        出栈，计算是否需要更新max_so_far
        同时，更新start为出栈的数字
    如果stack为空，
        start指向i的下一个位置
'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        start = 0
        max_so_far = 0
        stack = []
        for i in xrange(len(s)):
            if s[i] == "(":
                stack.append(min(i, start))
                start = i + 1
            else:
                if len(stack)>=1:
                    start = last = stack.pop()
                    max_so_far = max(i-last+1, max_so_far)
                else:
                    start = i + 1
        return max_so_far


def main():
    s = Solution()
    print s.longestValidParentheses("()()")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

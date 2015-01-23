# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

20: Valid Parentheses
https://oj.leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

===Comments by Dabay===
用一个stack来保存左括号，如果来的是对应的右括号，就pop一个；如果来的是不对应的右括号，直接return False。
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if (
                    (c == ")" and stack[-1] == "(") or
                    (c == "]" and stack[-1] == "[") or
                    (c == "}" and stack[-1] == "{")
                ):
                    stack.pop()
                else:
                    return False
        else:
            return len(stack) == 0


def main():
    sol = Solution()
    print sol.isValid("()[]{}")


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

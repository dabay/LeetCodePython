# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

65: Valid Number
https://oj.leetcode.com/problems/valid-number/

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
===Comments by Dabay===
感觉是一个自动机。DFA。
早就搞忘了，就用普通的办法判断吧。
然后想尝试一下用异常来判断，结果过了OJ。好吧，等以后再来想正常的解法。
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s)
        except Exception:
            return False
        return True


def main():
    sol = Solution()
    nums = ["0", " 0.1", "abc", "1 a", "2e10"]
    for num in nums:
        print "%s => %s" % (num, sol.isNumber(num))


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

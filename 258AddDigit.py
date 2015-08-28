# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
258: Add Digits
https://leetcode.com/problems/add-digits/

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

=== Comments by Dabay===
递归
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = num
        while num >= 10:
            res = 0
            while num > 0:
                res += num % 10
                num = num / 10
            num = res
        return res


def main():
    sol = Solution()
    print sol.addDigits(10)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
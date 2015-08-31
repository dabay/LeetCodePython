# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
263: Ugly Number
https://leetcode.com/problems/ugly-number/

Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

=== Comments by Dabay===
用几个遍历来记录是否还可能被2,3,5整除，减少模运算的次数。
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        div_2, div_3, div_5 = True, True, True
        while div_2 or div_3 or div_5:
            if div_2 and num % 2 == 0:
                num = num / 2
                continue
            else:
                div_2 = False
            if div_3 and num % 3 == 0:
                num = num / 3
                continue
            else:
                div_3 = False
            if div_5 and num % 5 == 0:
                num = num / 5
                continue
            else:
                div_5 = False
        return num == 1


def main():
    sol = Solution()
    print sol.isUgly(14)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
231: Power of Two
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.

=== Comments by Dabay===
一直除以2，直到1.
'''

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n / 2)


def main():
    sol = Solution()
    print sol.isPowerOfTwo(16)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
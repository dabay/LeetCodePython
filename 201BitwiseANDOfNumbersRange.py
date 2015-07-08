# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
200: Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
For example, given the range [5, 7], you should return 4.

=== Comments by Dabay===
如果range为1， 那么最后一位数肯定是0，如果是range为2，那么倒数第二比特也肯定是0...
所以如果range比m还大，结果肯定是0.
'''

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        if n - m >= m:
            return 0
        res = m
        for x in xrange(m+1, n+1):
            res = res & x
        return res


def main():
    sol = Solution()
    print sol.rangeBitwiseAnd(5, 7)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

126: Word Ladder II
https://leetcode.com/problems/word-ladder-ii/

Implement pow(x, n).

=== Comments by Dabay===
技巧在于用x的平方来让n减半。
同时注意n为负数的情况，以及n为奇数的情况。
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x == 0:
            return 0
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2:
            return self.pow(x*x, n/2) * x
        else:
            return self.pow(x*x, n/2)



def main():
    sol = Solution()
    print sol.pow(0.00001, 2147483647)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
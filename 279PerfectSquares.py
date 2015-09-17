# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
279: Perfect Squares
https://leetcode.com/problems/perfect-squares/

Given a positive integer n,
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

=== Comments by Dabay===
先建立一个squre numbers的列表，然后从最大数字的开始找，知道答案x之后继续，直到x个square number仍然小于n为止。
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        squares = [i*i for i in xrange(1, int(math.sqrt(n))+1)]
        squares = squares[::-1]
        print squares
        res = [n]
        self.find(squares, n, [], res, n)
        return res[0]

    def find(self, squares, target, tmp, res, n):
        if len(tmp) >= res[0]:
            return
        if target < 0:
            return
        if target == 0:
            print tmp
            res[0] = min(len(tmp), res[0])
        for i in squares:
            if target < i:
                continue
            tmp.append(i)
            self.find(squares, target-i, tmp, res, n)
            tmp.pop(-1)


def main():
    sol = Solution()
    print sol.numSquares(7168)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
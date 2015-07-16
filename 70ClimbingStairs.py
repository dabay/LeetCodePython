# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

70: Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

===Comments by Dabay===
每次只能一步或者两步，所以对于n步的时候，结果为sol(n-1)+sol(n-2),递归。这种解法会TLE。
那就从1开始往n来计算...DP
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = 0
        value1 = 1
        value2 = 2
        for i in xrange(n-2):
            res = value1 + value2
            value1 = value2
            value2 = res
        return res


def main():
    sol = Solution()
    print sol.climbStairs(4)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

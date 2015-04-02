# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

198: House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

=== Comments by Dabay===
DP. dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
dp数组和比num相比，前面多一个元素。
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        dp = [0] + [0 for _ in num]
        dp[1] = num[0]
        for i in xrange(1, len(num)):
            dp[i+1] = max(dp[i-1]+num[i], dp[i])
        return dp[-1]


def main():
    sol = Solution()
    num = [2,1,1,2]
    print sol.rob(num)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
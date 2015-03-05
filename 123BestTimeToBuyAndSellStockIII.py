# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

123: Best Time to Buy and Sell Stock III
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

=== Comments by Dabay===
计算两个数组，分别记录下标为i的时候，前面一半和后面一半的最大利润。

计算prices[0..i]的最大利润的时候，维护一个最小的price的变量，用当前price减去最小的price就是当前的卖掉的最大的利润，
    然后再和之前的最大利润做一次比较，大的那个数就是当前的最大的利润。
计算prices[i..<end>]实际就是前面的办法反过来，维护一个最大的price的变量...

接下来，判断每一个位置i，前后两半的利润在什么位置最大。

时间复杂度O(n*3),即O(n)。
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        first_transaction = [0 for _ in prices]
        min_price = prices[0]
        max_profit = 0
        for i in xrange(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            first_transaction[i] = max_profit

        second_transaction = [0 for _ in prices]
        max_price = prices[-1]
        max_profit = 0
        for i in xrange(len(prices)-2, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            second_transaction[i] = max_profit

        max_profit = 0
        for i in xrange(len(prices)):
            max_profit = max(first_transaction[i] + second_transaction[i], max_profit)

        return max_profit


def main():
    sol = Solution()
    prices = [1,2,0,4,5,6,7]
    print sol.maxProfit(prices)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

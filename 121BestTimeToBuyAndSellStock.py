# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the i<th> element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        profit = 0
        min_value = prices[0]
        for i in xrange(1, len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
                continue
            if prices[i] - min_value > profit:
                profit = prices[i] - min_value
                continue
        return profit


if __name__ == "__main__":
    s = Solution()
    prices = [2, 1, 2, 3, 2, 1]
    print s.maxProfit(prices)
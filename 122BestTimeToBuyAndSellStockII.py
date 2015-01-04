# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple
transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        profit = 0
        buy_value = prices[0]
        hold = False
        for i in xrange(1, len(prices)):
            if prices[i] == prices[i-1]:
                continue
            if prices[i-1] < prices[i] and hold is False:
                buy_value = prices[i-1]
                hold = True
                continue
            if prices[i-1] > prices[i] and hold is True:
                profit = profit + (prices[i-1] - buy_value)
                hold = False
                continue
        if hold is True:
            profit = profit + (prices[-1] - buy_value)
        return profit


if __name__ == "__main__":
    s = Solution()
    prices = [2, 1, 2, 3, 1, 2, 1]
    print s.maxProfit(prices)
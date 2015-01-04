# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the i<th> element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

虽然accept了，但是感觉好笨。 
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        profit = 0
        low_indexes = [0]
        high_indexes = [0]
        for i in xrange(1, len(prices)-1):
            if prices[i-1]==prices[i] and prices[i]==prices[i+1]:
                continue
            if prices[i-1]>=prices[i] and prices[i]<=prices[i+1]:
                low_indexes.append(i)
                continue
            if prices[i-1]<=prices[i] and prices[i]>=prices[i+1]:
                high_indexes.append(i)
                continue
        if prices[-2] > prices[-1]:
            low_indexes.append(len(prices)-1)
        else:
            high_indexes.append(len(prices)-1)

        for low_index in low_indexes:
            for high_index in high_indexes:
                if low_index >= high_index:
                    continue
                if prices[high_index] - prices[low_index] > profit:
                    profit = prices[high_index] - prices[low_index]

        return profit


if __name__ == "__main__":
    s = Solution()
    prices = [2, 1, 2, 3, 2, 1]
    print s.maxProfit(prices)
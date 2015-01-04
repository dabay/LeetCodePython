# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        temp = n
        while temp >= 5:
            temp = temp / 5
            result = result + temp
        return result

if __name__ == "__main__":
    s = Solution()
    n = 30
    print s.trailingZeroes(n)
    #import math
    #print math.factorial(n)
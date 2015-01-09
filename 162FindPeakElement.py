# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 1:
            return 0
        if num[0] > num[1]:
            return 0
        if num[-2] < num[-1]:
            return len(num) - 1
        for i in xrange(1, len(num)-1):
            if num[i-1] < num[i] and num[i] > num[i+1]:
                return i


def main():
    s = Solution()
    nums = [1, 5, 3, 1]
    print s.findPeakElement(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    end = time.clock()
    print "%s sec" % (end - start)

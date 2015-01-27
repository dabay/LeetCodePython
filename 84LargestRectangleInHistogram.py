# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

84: Largest Rectangle in Histogram
https://oj.leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

===Comments by Dabay===
遍历每个元素，每次往左右两边扩展，直到比这个元素小。然后计算更更新largest。
但是这个解法Time Limit Exceeded.
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        largest = 0
        i = 0
        while i < len(height):
            m = n = i
            h = height[i]
            while m-1>=0 and height[m-1]>=h:
                m -= 1
            while n+1<len(height) and height[n+1]>=h:
                n += 1
            largest = max(largest, h * (n-m+1))
            i += 1
        return largest


def main():
    sol = Solution()
    height = [2,1,5,6,2,3]
    print sol.largestRectangleArea(height)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

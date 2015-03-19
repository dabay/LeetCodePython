# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

42: Trapping Rain Water
https://oj.leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

===Comments by Dabay===
请参考：http://blog.csdn.net/wzy_1988/article/details/17752809
挨个分析每个A[i]能trapped water的容量，然后将所有的A[i]的trapped water容量相加即可
其次，对于每个A[i]能trapped water的容量，取决于A[i]左右两边的高度（可延展）较小值与A[i]的差值，
即volume[i] = [min(left[i], right[i]) - A[i]] * 1，这里的1是宽度，如果the width of each bar is 2,那就要乘以2了
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A) <= 2:
            return 0

        highest_on_left = [A[0] for _ in A]
        for i in xrange(1, len(A)):
            highest_on_left[i] = max(highest_on_left[i-1], A[i])

        highest_on_right = [A[-1] for _ in A]
        for i in xrange(len(A)-2, -1, -1):
            highest_on_right[i] = max(highest_on_right[i+1], A[i])

        res = 0
        for i in xrange(1, len(A)-1):
            res += min(highest_on_left[i], highest_on_right[i]) - A[i]
        return res


def main():
    s = Solution()
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    print s.trap(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

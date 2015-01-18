# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/first-missing-positive/
First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
===Comments by Dabay===
要求O(n)的时间，肯定不能常规排序，意思是只能扫描一次。
扫描的时候，如果是正数，就记录到一个hash表中。
最后从1开始到len(A)+1，在hash表中查找，第一个没有命中就是需要找的。
这里使用的空间不是constant，空间复杂度是O(n)。但是accept了，等以后再来考虑这个问题。
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        d = {}
        for i in xrange(len(A)):
            if A[i] > 0:
                d[A[i]] = True
        for x in xrange(1, len(A)+2):
            if x not in d:
                return x


def main():
    s = Solution()
    print s.firstMissingPositive([3,4,-1,1])


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



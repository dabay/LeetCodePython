# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

41: First Missing Positive
https://oj.leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.

===Comments by Dabay===
要求O(n)的时间，肯定不能常规排序，意思是只能扫描一次。
因为对空间有要求，所以只能在已经有的空间上做文章。

扫描的时候，当遇到正数，而且这个正数小于数组长度（因为如果大于数组长度，说明前面肯定缺少正数，同时也没有（无需）位置来存储它），
就把它交换到下标和它一样的位置上。
这样，扫描完成之后，从1的位置开始判断，如果位置k上存的数字不是k，这就是缺少的第一个正数。

这道题有三个需要注意的地方：
    -   交换之后，下标不能移动，需要继续判断。
    -   可能从1开始到最后都没有缺少的正数，此时下一个正数可能放在第一个位置上。
    -   当数组长度为0时，直接返回1.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if len(A) == 0:
            return 1
        i = 0
        while i < len(A):
            if A[i] > 0 and A[i] < len(A) and A[A[i]] != A[i]:
                A[A[i]], A[i] = A[i], A[A[i]]
            else:
                i = i + 1
        for x in xrange(1, len(A)):
            if A[x] != x:
                return x
        else:
            if A[0] == len(A):
                return len(A) + 1
            else:
                return len(A)


def main():
    s = Solution()
    print s.firstMissingPositive([3,4,-1,1])


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

88: Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements
from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

===Comments by Dabay===
这里的解法不是in-place的。
'''

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        tmp = [None for _ in xrange(m+n)]
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tmp[k] = nums1[i]
                i += 1; k += 1
            else:
                tmp[k] = nums2[j]
                j += 1; k += 1
        if i == m:
            while k < m + n:
                tmp[k] = nums2[j]
                j += 1; k += 1
        else:
            while k < m + n:
                tmp[k] = nums1[i]
                i += 1; k += 1
        for i in xrange(m+n):
            nums1[i] = tmp[i]


def main():
    sol = Solution()
    nums1 = [1,2,3]
    nums2 = [0,4,5]
    sol.merge(nums1, 0, nums2, 1)
    print nums1


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

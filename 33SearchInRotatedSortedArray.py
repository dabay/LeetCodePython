# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

33: Search in Rotated Sorted Array
https://oj.leetcode.com/problems/search-in-rotated-sorted-array/

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

===Comments by Dabay===
解法一：（可以过OJ）
首先判断是否应该从前往后，还是从后往前。
取决于和第一个数的判断，如果比第一个数小，就从后往前；如果比第一个数大，就从前往后。
注意一些继续循环的条件：
从前往后的时候：下标有效、递增、目标比上一个大
从后往前的时候：下标有效、递减、目标比上一个小

解法二：（二分查找）
把中位数标记出来。
如果中位数比左边大，说明左边是递增的，断点在右边：
    如果target在左边递增的区间，就在左边查找；
    否则，在右边查找
如果中位数比左边小，说明右边是递增的，断点在左边：
    如果target在右边的递增区间，就在右边查找；
    否则，在左边查找。

从跑的结果来看，对于小数据来说，解法一速度还快一点点。
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left, right = 0, len(A)-1
        while left <= right:
            if A[left] == target:
                return left
            if A[right] == target:
                return right
            m = (left + right) / 2
            mid = A[m]
            if mid == target:
                return m
            if mid > A[left]:
                if A[left]< target and target < A[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if A[m] < target and target < A[right]:
                    left = m + 1
                else:
                    right = m - 1
        else:
            return -1


    # def search(self, A, target):
    #     if len(A) == 1:
    #         return [-1, 0][A[0]==target]
    #
    #     if A[0] == target:
    #         return 0
    #     elif A[0] < target:
    #         i = 1
    #         while i < len(A) and A[i-1] < A[i] and A[i-1] < target:
    #             if A[i] == target:
    #                 return i
    #             i = i + 1
    #         else:
    #             return -1
    #     else:
    #         if A[-1] == target:
    #             return len(A) - 1
    #         i = len(A) - 2
    #         while i >= 0 and A[i] < A[i+1] and target < A[i+1]:
    #             if A[i] == target:
    #                 return i
    #             i = i - 1
    #         else:
    #             return -1


def main():
    s = Solution()
    nums = [4,5,6,7,8,1,2,3]
    print s.search(nums, 8)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



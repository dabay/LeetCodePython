# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
===Comments by Dabay===
搞不懂这道题为什么是hard，逻辑很简单。
首先判断是否应该从前往后，还是从后往前。
取决于和第一个数的判断，如果比第一个数小，就从后往前；如果比第一个数大，就从前往后。

注意一些退出条件：
从前往后的时候：下标有效、递增、目标比上一个大
从后往前的时候：下标有效、递减、目标比上一个小
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 1:
            return [-1, 0][A[0]==target]

        if A[0] == target:
            return 0
        elif A[0] < target:
            i = 1
            while i < len(A) and A[i-1] < A[i] and A[i-1] < target:
                if A[i] == target:
                    return i
                i = i + 1
            else:
                return -1
        else:
            if A[-1] == target:
                return len(A) - 1
            i = len(A) - 2
            while i >= 0 and A[i] < A[i+1] and target < A[i+1]:
                if A[i] == target:
                    return i
                i = i - 1
            else:
                return -1


def main():
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print s.search(nums, 1)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



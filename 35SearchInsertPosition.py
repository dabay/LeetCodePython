# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

35: Search Insert Position
https://oj.leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

===Comments by Dabay===
二分查找。
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left, right = 0, len(A)-1
        while left < right:
            m = (left + right) / 2
            if A[m] == target:
                return m
            elif A[m] < target:
                left = m + 1
            else:
                right = m - 1
        else:
            return [left, left + 1][target > A[left]]


def main():
    sol = Solution()
    nums = [1,3,5,6]
    target = 5
    print sol.searchInsert(nums, target)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
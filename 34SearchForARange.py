# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

34: Search for a Range
https://oj.leetcode.com/problems/search-for-a-range/

Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

===Comments by Dabay===
二分查找。
当target在中间的时候，往两边扩展。
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        def expend(nums, index):
            left = right = index
            while left - 1 >= 0 and nums[left - 1] == nums[index]:
                left -= 1
            while right + 1 < len(nums) and nums[right + 1] == nums[index]:
                right += 1
            return [left, right]

        l, r = 0, len(A) - 1
        while l <= r:
            m = (l + r) /2
            if A[m] == target:
                return expend(A, m)
            elif A[m] < target:
                l = m + 1
            else:
                r = m - 1
        else:
            return [-1, -1]


def main():
    sol = Solution()
    nums = [2,2]
    target = 2
    print sol.searchRange(nums, target)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
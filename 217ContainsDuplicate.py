# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

=== Comments by Dabay===
使用hash table
'''

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        h = {}
        for n in nums:
            if n in h:
                return True
            else:
                h[n] = 1
        else:
            return False


def main():
    nums = [1,5,2,3,4,5,6,2,2]
    sol = Solution()
    print sol.containsDuplicate(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
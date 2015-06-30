# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
219: Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k, find out whether there there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

=== Comments by Dabay===
使用一个大小为k的队列,会Time Limit Exceed。
还是使用hash，记录上一次出现的位置。
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        h = {}
        for i in xrange(len(nums)):
            if nums[i] in h:
                if i - h[nums[i]] <= k:
                    return True
            h[nums[i]] = i
        else:
            return False


def main():
    nums = [1,5,2,3,4,5,6,2,1,5,3,2]
    sol = Solution()
    print sol.containsNearbyDuplicate(nums, 3)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

268: Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2. 

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

用完整的等差数列的和 减去 现有的数列的和
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for x in nums:
            s += x
        s2 = (0 + len(nums)) * (len(nums)+1) / 2
        return s2 - s



def main():
    sol = Solution()
    nums = [0, 1, 2, 3, 5]
    print sol.missingNumber(nums)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

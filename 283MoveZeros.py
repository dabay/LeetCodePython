# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i1 = 0
        while True:
            while i1 < len(nums) and nums[i1] <> 0:
                i1 += 1
            i2 = i1 + 1
            while i2 < len(nums) and nums[i2] == 0:
                i2 += 1
            if i1 == len(nums) or i2 == len(nums):
                return
            else:
                nums[i1], nums[i2] = nums[i2], nums[i1]

def main():
    sol = Solution()
    nums = [4,2,4,0,0,3,0,5,1,0]
    sol.moveZeroes(nums)
    print nums


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
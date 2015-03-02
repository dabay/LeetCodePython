# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

189: Rotate Array
https://oj.leetcode.com/problems/rotate-array/

Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Hint:
Could you do it in-place with O(1) extra space?

===Comments by Dabay===
trick是交换三次，第一次把字符串全部反转，第二次反转前面k个，第三次反转后面剩余的。
'''

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        def reverse(nums, index_left, index_right):
            while index_left < index_right:
                nums[index_left], nums[index_right] = nums[index_right], nums[index_left]
                index_left += 1
                index_right -= 1

        if k > len(nums):
            k = k % len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)


def main():
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol.rotate(nums, k)
    print nums


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

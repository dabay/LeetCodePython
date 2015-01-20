# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

16: 3Sum Closest
https://oj.leetcode.com/problems/3sum-closest/

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

===Comments by Dabay===
先排序，然后从左到右固定一个数，在后边的数列中使用左右指针往中间靠拢的方法查找。
当比之前更接近target的时候，更新找个这个值。

从左往右固定一个数,左右两个指针往中间靠拢。
'''
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) < 3:
            return []
        num.sort()
        closest = num[0] + num[1] + num[2]
        difference = abs(target - closest)
        for i in xrange(len(num)-2):
            j, k = i+1, len(num)-1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if abs(target - sum) < difference:
                    closest = sum
                    difference = abs(target - sum)
                if sum == target:
                    return sum
                elif sum < target:
                    j = j + 1
                else:
                    k = k - 1
        return closest


def main():
    sol = Solution()
    nums = [-3,0,1,2]
    solution = sol.threeSumClosest(nums, 1)
    print solution


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
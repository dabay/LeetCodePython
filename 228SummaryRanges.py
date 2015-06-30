# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
228: Summary Ranges
https://leetcode.com/problems/summary-ranges/

Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

=== Comments by Dabay===
判断连续, 注意输入长度为0或者1的情况，还有处理到最后的情况。
感觉代码有点多，应该有更简单的方法。
'''

# Definition for a binary tree node.
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        start = nums[0]
        res = []
        for i in xrange(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                continue
            else:
                if start == nums[i-1]:
                    res.append("{}".format(start))
                else:
                    res.append("{0}->{1}".format(start, nums[i-1]))
                start = nums[i]
        else:
            if start == nums[-1]:
                res.append("{}".format(nums[-1]))
            else:
                res.append("{0}->{1}".format(start, nums[-1]))
        return res


def main():
    nums = [0,1,2,4,5,7]
    sol = Solution()
    print sol.summaryRanges(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
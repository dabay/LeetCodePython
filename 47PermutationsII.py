# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

47: Permutations II
https://oj.leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

===Comments by Dabay===
先排序，然后DFS。
注意去重，如果进入了一次DFS，用pre记录上次用的数字。这个pre只在DFS中的for中有效，所以每次进入进入新的DFS的时候，重新设置为None.
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        res = []
        num.sort()
        self.DFS(res, [], None, num)
        return res

    def DFS(self, res, l, pre, nums):
        if len(nums) == 0:
            res.append(list(l))
        pre = None
        for i in xrange(len(nums)):
            if nums[i] == pre:
                continue
            l.append(nums[i])
            self.DFS(res, l, nums[i], nums[:i] + nums[i+1:])
            l.pop()
            pre = nums[i]


def main():
    sol = Solution()
    nums = [1,1,2]
    print sol.permuteUnique(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
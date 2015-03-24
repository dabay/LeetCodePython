# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

46: Permutations
https://leetcode.com/problems/permutations/

Given a collection of numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

=== Comments by Dabay===
DFS.
注意的问题是，
    加入到res结果集中的时候，做一个l的拷贝。
    DSF之后恢复l的状态。
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        res = []
        self.DFS(res, [], num)
        return res

    def DFS(self, res, l, nums):
        if len(nums) == 0:
            res.append(list(l))
        for i in xrange(len(nums)):
            l.append(nums[i])
            self.DFS(res, l, nums[:i] + nums[i+1:])
            l.pop()


def main():
    sol = Solution()
    num = [1, 2, 3]
    print sol.permute(num)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
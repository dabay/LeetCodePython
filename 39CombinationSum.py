# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

39: Combination Sum
https://oj.leetcode.com/problems/combination-sum/

Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

===Comments by Dabay===
递归。
先把candidates排序。
遍历candidates，用index来记录目前的指针。
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        def combinationSum2(candidates, target, index, res, res_list):
            if target == 0:
                res_list.append(list(res))
                return
            while index < len(candidates) and target >= candidates[index]:
                res.append(candidates[index])
                combinationSum2(candidates, target-candidates[index], index, res, res_list)
                res.pop()
                index += 1

        res_list = []
        candidates.sort()
        combinationSum2(candidates, target, 0, [], res_list)
        return res_list


def main():
    sol = Solution()
    candidates = [1,2]
    target = 4
    print sol.combinationSum(candidates, target)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)





# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

40: Combination Sum II
https://oj.leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

===Comments by Dabay===
递归。
先把candidates排序。
遍历candidates，用index来记录目前的指针。
注意去掉结果集中可能的重复。
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        def combinationSum(candidates, target, index, res, res_list):
            if target == 0:
                if res not in res_list:
                    res_list.append(list(res))
                return
            while index < len(candidates) and target >= candidates[index]:
                res.append(candidates[index])
                combinationSum(candidates, target-candidates[index], index+1, res, res_list)
                res.pop()
                index += 1

        res_list = []
        candidates.sort()
        combinationSum(candidates, target, 0, [], res_list)
        return res_list


def main():
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print sol.combinationSum2(candidates, target)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)


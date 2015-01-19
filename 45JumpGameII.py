# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

45: Jump Game II
https://oj.leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

===Comments by Dabay===
上一次的最远边界，与这一步能够达到的最远边界组成一个范围段。这是第N步能够到的最远范围。
如果这个范围超过了数组的边界，返回步数。
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) <= 1:
            return 0
        last_index = len(A) - 1
        min_index = 1
        max_index = A[0]
        step = 1
        if max_index >= last_index:
            return step
        while True:
            new_max_index = min_index
            step = step + 1
            for index in xrange(min_index, max_index+1):
                reach = index + A[index]
                new_max_index = max(new_max_index, reach)
                if new_max_index >= last_index:
                    return step
            else:
                min_index, max_index = max_index+1, new_max_index


def main():
    s = Solution()
    print s.jump([2,3,0,1,4])


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



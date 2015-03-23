# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

55: Jump Game
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

=== Comments by Dabay===
每次计算能到达的新范围。
如果新的范围超越了len(A)-1就范围True.
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) <= 1:
            return True
        start = 0
        end = start + A[start]
        while end >= start:
            if end >= len(A) - 1:
                return True
            new_end = end
            for i in xrange(start, end+1):
                new_end = max(new_end, i + A[i])
            start, end = end+1, new_end
        else:
            return False


def main():
    sol = Solution()
    A = [1,1,1,0]
    print sol.canJump(A)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
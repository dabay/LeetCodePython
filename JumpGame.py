# -*- coding: utf8 -*-
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def canJump(self, A):
        if len(A) == 0:
            return False

        max_reach = A[0]
        i = 0
        while i <= max_reach:
            if i + A[i] > max_reach:
                max_reach = i + A[i]
            if max_reach >= len(A)-1:
                return True
            i = i + 1

        return False


if __name__ == "__main__":
    s = Solution()
    input = [1,1,1,0]
    print s.canJump(input)



  

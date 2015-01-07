# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/single-number-ii/

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

不知道为什么这个能够Accept,排序能在线性的时间和不用格外空间的情况下完成？
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 1:
            return A[0]
        A.sort()
        print A
        for i in xrange(1, len(A)-1):
            if A[i-1] != A[i] and A[i] != A[i+1]:
                return A[i]
        if A[0] != A[1]:
            return A[0]
        else:
            return A[-1]


def main():
    s = Solution()
    print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)
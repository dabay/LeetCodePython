# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

53: Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

=== Comments by Dabay===
一维动态规划。
二分法的基本思想是：从中间分开，两边分别递归，同时处理跨界的情况。
http://www.cnblogs.com/springfor/p/3877058.html
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return 0
        max_so_far = max_ending_here = A[0]
        for i in xrange(1, len(A)):
            max_ending_here = max(max_ending_here + A[i], A[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


def main():
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print sol.maxSubArray(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/maximum-product-subarray/

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        max_ending_here = A[0]
        min_ending_here = A[0]
        max_so_far = A[0]
        for i in xrange(1, len(A)):
            tmp_max_ending_here = max(max(min_ending_here*A[i], max_ending_here*A[i]), A[i])
            tmp_min_ending_here = min(min(min_ending_here*A[i], max_ending_here*A[i]), A[i])
            max_so_far = max(max_so_far, tmp_max_ending_here)
            max_ending_here, min_ending_here = tmp_max_ending_here, tmp_min_ending_here
        return max_so_far


def main():
    s = Solution()
    nums = [0, 2]
    print s.maxProduct(nums)

if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    end = time.clock()
    print "%s sec" % (end - start)
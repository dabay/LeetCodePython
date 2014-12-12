# -*- coding: utf8 -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

该问题最初由布朗大学的Ulf Grenander教授于1977年提出，当初他为了展示数字图像中一个简单的最
大然似然估计模型。不久之后卡内基梅隆大学的Jay Kadane提出了该问题的线性算法。（Bentley 1984）。
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_to_here = A[0]
        max_so_far = A[0]
        for x in A[1:]:
            max_to_here = max(x, max_to_here + x)
            max_so_far = max(max_so_far, max_to_here)
        return max_so_far

if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


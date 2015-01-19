# -*- coding: utf8 -*-
'''
Trapping Rain Water
https://oj.leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

===Comments by Dabay===
臃肿的解法，没什么好说的。等下次优化之后再写评论。
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        def find_right_index(left_pole_index, A):
            right_pole_index = left_pole_index + 1
            while right_pole_index < len(A):
                if A[right_pole_index] >= A[left_pole_index]:
                    return  right_pole_index
                right_pole_index = right_pole_index + 1
            else:
                return right_pole_index

        def trap_water(left_pole_index, right_pole_index, A):
            water = 0
            left_pole = A[left_pole_index]
            index = left_pole_index + 1
            while index < right_pole_index:
                water = water + (left_pole - A[index])
                index = index + 1
            return water

        def find_max_index(A):
            max_index = 0
            for i in xrange(len(A)):
                if A[max_index] < A[i]:
                    max_index = i
            return max_index

        def trap2(part):
            if part is None or len(part) <= 2:
                return 0
            water = 0
            left_pole_index = 0
            while left_pole_index < len(part)-2:
                right_pole_index = find_right_index(left_pole_index, part)
                if right_pole_index < len(part):
                    water = water + trap_water(left_pole_index, right_pole_index, part)
                    left_pole_index = right_pole_index
                else:
                    left_pole_index = left_pole_index + 1
            return water

        if len(A) <= 2:
            return 0

        max_index = find_max_index(A)
        left_part = A[:max_index+1]
        right_part = A[max_index:]
        right_part.reverse()

        return trap2(left_part) + trap2(right_part)


def main():
    s = Solution()
    nums = [4,2,3]
    print s.trap(nums)

if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

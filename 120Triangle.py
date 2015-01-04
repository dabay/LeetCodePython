# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/triangle/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

如果需要O(n)的空间，可以一行一行地计算得到一个最小路径的list就是了。
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        def min_list(triangle):
            if len(triangle) == 0:
                return None
            if len(triangle) == 1:
                return triangle[0]
            upper_min_list = min_list(triangle[:-1])
            bottom_list = triangle[-1]
            result = []
            result.append(upper_min_list[0]+bottom_list[0])
            for i in xrange(1, len(bottom_list)-1):
                result.append(bottom_list[i] + min(upper_min_list[i-1], upper_min_list[i]))
            result.append(upper_min_list[-1]+bottom_list[-1])
            return result

        bottom_list = min_list(triangle)
        minimum = bottom_list[0]
        for i in xrange(1, len(bottom_list)):
            if minimum > bottom_list[i]:
                minimum = bottom_list[i]
        return minimum


if __name__ == "__main__":
    s = Solution()
    triangle = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    print s.minimumTotal(triangle)
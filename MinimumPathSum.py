# -*- coding: utf8 -*-
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
    the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        # init first row
        for i in xrange(1, len(grid[0])):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        # init first column
        for j in xrange(1, len(grid)):
            grid[j][0] = grid[j-1][0] + grid[j][0]

        for r in xrange(1, len(grid)):
            for c in xrange(1, len(grid[0])):
                grid[r][c] = grid[r][c] + min(grid[r][c-1], grid[r-1][c])

        return grid[-1][-1]


if __name__ == "__main__":
    s = Solution()
    grid = [
        [1,1],
        [2,1]
    ]
    print s.minPathSum(grid)



  

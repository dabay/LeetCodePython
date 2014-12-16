# -*- coding: utf8 -*-
'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        matrix = []
        for i in xrange(m-1):
            row = []
            for j in xrange(n):
                row.append(0)
            row[-1] = 1
            matrix.append(row)
        last_row = [1 for i in xrange(n)]
        matrix.append(last_row)

        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        return matrix[0][0]


if __name__ == "__main__":
    s = Solution()
    print s.uniquePaths(3, 7)






  

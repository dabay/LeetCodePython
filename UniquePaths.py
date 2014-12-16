# -*- coding: utf8 -*-
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        def add_down_right(x, y, matrix, obstacleGrid):
            if obstacleGrid[x][y] == 1:
                return 0
            else:
                return matrix[i+1][j] + matrix[i][j+1]


        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        matrix = []
        for i in xrange(m):
            row = []
            for j in xrange(n):
                row.append(0)
            matrix.append(row)

        obstacle = False
        for i in xrange(n-1, -1, -1):
            if obstacle is False:
                if obstacleGrid[m-1][i] != 1:
                    matrix[m-1][i] = 1
                else:
                    obstacle = True
                    matrix[m-1][i] = 0
            else:
                matrix[m-1][i] = 0

        obstacle = False
        for i in xrange(m-1, -1, -1):
            if obstacle is False:
                if obstacleGrid[i][n-1] != 1:
                    matrix[i][n-1] = 1
                else:
                    obstacle = True
                    matrix[i][n-1] = 0
            else:
                matrix[i][n-1] = 0

        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                matrix[i][j] = add_down_right(i, j, matrix, obstacleGrid)
        return matrix[0][0]


if __name__ == "__main__":
    s = Solution()
    obstacle_grid = [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    print s.uniquePathsWithObstacles(obstacle_grid)






  

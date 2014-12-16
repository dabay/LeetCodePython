# -*- coding: utf8 -*-
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
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






  

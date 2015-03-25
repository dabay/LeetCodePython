# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

48: Rotate Image
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Could you do this in-place?

=== Comments by Dabay===
画一个图，先按照左上到右下的斜线翻转，然后再按照竖对称轴翻转。
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        dimension = len(matrix)
        for i in xrange(dimension):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(dimension):
            for j in xrange(dimension/2):
                matrix[i][j], matrix[i][dimension-1-j] = matrix[i][dimension-1-j], matrix[i][j]


def main():
    sol = Solution()
    matrix = [
        [1,2],
        [3,4]
    ]
    sol.rotate(matrix)
    print matrix

if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
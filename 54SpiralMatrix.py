# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

54: Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

=== Comments by Dabay===
一圈一圈的处理，一共处理n/2圈。
注意一些细节，比如圈数，还有同一圈不要重复。
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [i[0] for i in matrix]
        height = len(matrix)
        width = len(matrix[0])
        res = []
        n = 0
        while n < (min(height, width)+1)/2:
            for i in xrange(n, width-n):
                res.append(matrix[n][i])
            for i in xrange(n+1, height-n):
                res.append(matrix[i][width-1-n])
            if n < height-n-1:
                for i in reversed(xrange(n, width-n-1)):
                    res.append(matrix[height-n-1][i])
                for i in reversed(xrange(n+1, height-n-1)):
                    res.append(matrix[i][n])
            n += 1
        return res


def main():
    sol = Solution()
    matrix = [
     [2, 3]
    ]
    print sol.spiralOrder(matrix)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
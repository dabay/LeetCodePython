# -*- coding: utf8 -*-
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def spiralOrder(self, matrix):
        def spiral_order(result, matrix, start_x, start_y, m, n):
            if n==0 or m==0:
                return
            if n == 1:
                for i in xrange(m):
                    result.append(matrix[start_x+i][start_y])
                return
            if m == 1:
                for i in xrange(n):
                    result.append(matrix[start_x][start_y+i])
                return


            for i in xrange(start_y, start_y+n):
                result.append(matrix[start_x][i])
            for i in xrange(start_x+1, start_x+m):
                result.append(matrix[i][start_y+n-1])
            for i in xrange(start_y+n-1-1, start_y-1, -1):
                result.append(matrix[start_x+m-1][i])
            for i in xrange(start_x+m-1-1, start_x, -1):
                result.append(matrix[i][start_y])

            return spiral_order(result, matrix, start_x + 1, start_y + 1, m-2, n-2)

        if len(matrix) == 0:
            return []
        result = []
        spiral_order(result, matrix, 0, 0, len(matrix), len(matrix[0]))
        return result


if __name__ == "__main__":
    s = Solution()
    input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print s.spiralOrder(input)

  

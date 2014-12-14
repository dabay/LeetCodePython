# -*- coding: utf8 -*-
'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
     # @return a list of lists of integer
    def generateMatrix(self, n):
        def init_matrix(n):
            matrix = []
            for i in xrange(n):
                row_list = []
                for i in xrange(n):
                    row_list.append(0)
                matrix.append(row_list)
            return matrix

        def generate_layer(matrix, layer, n, start):
            if matrix[layer][layer] != 0:
                return

            for i in xrange(n):
                matrix[layer][layer+i] = start
                start = start + 1
            for i in xrange(1, n):
                matrix[layer+i][layer+n-1] = start
                start = start + 1
            for i in xrange(n-2, -1, -1):
                matrix[layer+n-1][layer+i] = start
                start = start + 1
            for i in xrange(n-2, 0, -1):
                matrix[layer+i][layer] = start
                start = start + 1

            return generate_layer(matrix, layer+1, n-2, start)

        if n == 0:
            return []
        if n == 1:
            return [[1]]
        matrix = init_matrix(n)
        generate_layer(matrix, 0, n, 1)
        return matrix


if __name__ == "__main__":
    s = Solution()
    print s.generateMatrix(1)

  

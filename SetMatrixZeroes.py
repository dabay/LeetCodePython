# -*- coding: utf8 -*-
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
哎，这道题有点巧妙呐~
'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row_count = len(matrix)
        column_count = len(matrix[0])

        first_row_zero = False
        for c in xrange(column_count):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        first_column_zero = False
        for r in xrange(row_count):
            if matrix[r][0] == 0:
                first_column_zero = True
                break

        for r in xrange(1, row_count):
            for c in xrange(1, column_count):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in xrange(1, row_count):
            for c in xrange(1, column_count):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_zero is True:
            for c in xrange(column_count):
                matrix[0][c] = 0

        if first_column_zero is True:
            for r in xrange(row_count):
                matrix[r][0] = 0



if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    print s.setZeroes(matrix)
    print matrix



  

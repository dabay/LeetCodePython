# -*- coding: utf8 -*-
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    *   Integers in each row are sorted from left to right.
    *   The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        search_row_index = 0
        for r in xrange(len(matrix)):
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] > target:
                break
            else:
                search_row_index = r

        for c in xrange(1, len(matrix[0])):
            if matrix[search_row_index][c] == target:
                return True
            elif matrix[search_row_index][c] > target:
                return False
            else:
                continue

        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [
      [1]
    ]
    print s.searchMatrix(matrix, 1)




  

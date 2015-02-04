# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

36: Valid Sudoku
https://oj.leetcode.com/problems/valid-sudoku/

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

===Comments by Dabay===
先检查每个3x3的格子。
然后遍历board，当遇到数字时，检查其所在的行和列。这里用d_row和d_col记录检查过的行和列，避免重复检查。
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                d = {}
                for x in xrange(i, i+3):
                    for y in xrange(j, j+3):
                        if board[x][y] == '.':
                            continue
                        n = board[x][y]
                        if n in d:
                            return False
                        d[n] = True

        d_row = {}
        d_col = {}
        for i in xrange(0, 9):
            for j in xrange(0, 9):
                if board[i][j] == '.':
                    continue
                num = board[i][j]
                if i not in d_row:
                    d = {}
                    for x in xrange(0, 9):
                        if board[i][x] == '.':
                            continue
                        n = board[i][x]
                        if n in d:
                            return False
                        d[n] = True
                    d_row[i] = True
                if j not in d_col:
                    d = {}
                    for y in xrange(0, 9):
                        if board[y][j] == '.':
                            continue
                        n = board[y][j]
                        if n in d:
                            return False
                        d[n] = True
                    d_col[j] = True
        return True


def main():
    sol = Solution()
    board = [
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79"
    ]
    print sol.isValidSudoku(board)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

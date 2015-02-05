# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

37: Sudoku Solver
https://oj.leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.

===Comments by Dabay===
逐行扫描，当遇到“.”的时候，尝试每一个可能的valid_num。
如果能DFS到底，就return True；否则，把这个位置重置为“.”，进行下一次尝试。
'''

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def next_position(position):
            i, j = position
            j += 1
            if j >= 9:
                j -= 9
                i += 1
            return (i, j)

        def valid_nums(board, position):
            i, j = position
            s = [str(n) for n in xrange(1, 10)]
            for row in xrange(9):
                if board[row][j] != '.' and board[row][j] in s:
                    s.remove(board[row][j])
            for col in xrange(9):
                if board[i][col] != '.' and board[i][col] in s:
                    s.remove(board[i][col])
            ii = i / 3
            jj = j / 3
            for row in xrange(3):
                for col in xrange(3):
                    if board[ii*3+row][jj*3+col] != '.' and board[ii*3+row][jj*3+col] in s:
                        s.remove(board[ii*3+row][jj*3+col])
            return s

        def solveSudoku2(board, position):
            i, j = position
            if i == 9:
                return True
            if board[i][j] == '.':
                nums = valid_nums(board, position)
                for n in nums:
                    board[i][j] = n
                    if solveSudoku2(board, next_position(position)) is True:
                        return True
                    board[i][j] = '.'
            else:
                return solveSudoku2(board, next_position(position))

        solveSudoku2(board, (0, 0))


def print_board(board):
    print "-" * 30
    for row in board:
        for x in row:
            print "%s " % x,
        print
    print "-" * 30


def main():
    s = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print_board(board)
    s.solveSudoku(board)
    print_board(board)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)





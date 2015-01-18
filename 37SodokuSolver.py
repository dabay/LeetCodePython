# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/sudoku-solver/
Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
===Comments by Dabay===
把需要填写的空缺记录下来。
一个个的试，深度优先算法，试的时候计算可能的数字。
'''

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def cell_nums(row, col, board):
            nums = [str(i) for i in xrange(1,10)]
            r_div = int(row / 3) * 3
            c_div = int(col / 3) * 3
            for r in xrange(r_div, r_div+3):
                for c in xrange(c_div, c_div+3):
                    x = board[r][c]
                    if x in nums:
                        nums.remove(x)
            for i in xrange(9):
                if board[row][i] in nums:
                    nums.remove(board[row][i])
                if board[i][col] in nums:
                    nums.remove(board[i][col])
            return nums

        def fill(to_fill, board, res):
            if len(to_fill) == 0:
                res[0] = True
                return

            (row, col) = to_fill.pop(0)
            possible_nums = cell_nums(row, col, board)
            for num in possible_nums:
                board[row][col] = num
                fill(to_fill, board, res)
                if res[0] == True:
                    return
            to_fill.insert(0, (row, col))
            board[row][col] = "."


        to_fill = []
        for r in xrange(len(board)):
            for c in xrange(len(board[r])):
                if board[r][c] == ".":
                    to_fill.append((r,c))
        res = [False]
        fill(to_fill, board, res)


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
    s.solveSudoku(board)
    print_board(board)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



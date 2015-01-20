# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

51: N-Queens
https://oj.leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
===Comments by Dabay===
这套题思路比较简单，先发一个皇后，然后找下一个可能的位置放第二个...

技巧就在“找下一个可能的位置”上，
    - 下一个位置，其实就在下一行中
    - 检查是否可以放置的时候，只需要检查所在列是否被占用，以及分别向左上和右上是否斜线被占。（因为下面还没有放皇后呐）
'''
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def make_solution(board):
            copy = []
            for row in board:
                row_str = ""
                for c in row:
                    row_str = row_str + c
                copy.append(row_str)
            return copy

        def check_up(r, c, queen_stack, board):
            i = 1
            while i < len(board):
                if r-i>=0 and c-i>=0 and board[r-i][c-i]=='Q':
                    return False
                if r-i>=0 and c+i<len(board) and board[r-i][c+i]=="Q":
                    return False
                i = i + 1
            else:
                return True

        def find_available_positions(board, queen_stack):
            positions = []
            row = len(queen_stack)
            queen_columns = [pos[1] for pos in queen_stack]
            for c in xrange(len(board)):
                if c in queen_columns:
                    continue
                if board[row][c] == "." and check_up(row, c, queen_stack, board):
                    positions.append((row,c))
            return positions

        def DFS(board, queen_stack, res):
            if len(queen_stack) >= len(board):
                res.append(make_solution(board))
                return
            positions = find_available_positions(board, queen_stack)
            for (r, c) in positions:
                queen_stack.append((r, c))
                board[r][c] = "Q"
                DFS(board, queen_stack, res)
                queen_stack.pop()
                board[r][c] = "."


        board = [["."] * n for _ in xrange(n)]
        queen_stack = []
        res = []

        DFS(board, queen_stack, res)
        return res


def print_board(board):
    print '-' * 30
    for row in board:
        for item in row:
            print item,
        print
    print '-' * 30


def main():
    sol = Solution()
    solutions = sol.solveNQueens(4)
    for solution in solutions:
        print_board(solution)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
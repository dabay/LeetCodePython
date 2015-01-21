# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

52: N-Queens II
https://oj.leetcode.com/problems/n-queens-ii/

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
===Comments by Dabay===
不知道和N Queen相比有没有简单很多的方法。我这里的解法思路和N Queen一样的。

一个一个放皇后，知道能放下最后一个皇后，解法+1。
放第k个皇后的时候，在第k行中找位置，先看列被占用没有，然后往左上和右上看斜线被占用没有。
'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        def check_up(r, c, board):
            for row in xrange(r):
                if board[row][c] == 'Q':
                    return False
            else:
                return True

        def check_upleft(r, c, board):
            row = r - 1
            column = c - 1
            while row>=0 and column>=0:
                if board[row][column] == 'Q':
                    return False
                row = row - 1
                column = column - 1
            else:
                return True

        def check_upright(r, c, board):
            row = r - 1
            column = c + 1
            while row>=0 and column<len(board):
                if board[row][column] == 'Q':
                    return False
                row = row - 1
                column = column + 1
            else:
                return True

        def DFS(board, queens, res):
            if queens == 0:
                res[0] = res[0] + 1
                return
            r = len(board) - queens
            for c in xrange(len(board)):
                if not check_up(r, c, board) or not check_upleft(r, c, board) or not check_upright(r, c, board):
                    continue
                else:
                    board[r][c] = 'Q'
                    DFS(board, queens-1, res)
                    board[r][c] = '.'


        board = [['.'] * n for _ in xrange(n)]
        #print board
        queens = n
        res = [0]
        DFS(board, queens, res)
        return res[0]


def main():
    sol = Solution()
    print sol.totalNQueens(5)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

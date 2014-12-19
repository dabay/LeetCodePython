# -*- coding: utf8 -*-
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
这里给的例子有问题，实际上测试的board中的字符串没有放在列表中。board is actually like ["ABCE","SFCS","ADEE"]
怪说不得这道题的通过率比较低...
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def change_to_2d_matrix(board):
            for r in xrange(len(board)):
                row = []
                for c in xrange(len(board[r])):
                    row.append(str(board[r][c]))
                board[r] = row

        def find_start_points(board, letter):
            #print letter
            start_points = []
            for r in xrange(len(board)):
                for c in xrange(len(board[r])):
                    if board[r][c] == letter:
                        start_points.append((r,c))
            return start_points

        def search_word(board, been_map, r, c, letters, letter_index):
            if (r, c) in been_map or r < 0 or c < 0 or c >= len(board[0]) or r >= len(board):
                return False
            if board[r][c] != letters[letter_index]:
                return False

            if letter_index == len(letters)-1:
                return True
            else:
                been_map.append((r, c))
                return (
                    search_word(board, list(been_map), r-1, c, letters, letter_index+1) or
                    search_word(board, list(been_map), r+1, c, letters, letter_index+1) or
                    search_word(board, list(been_map), r, c+1, letters, letter_index+1) or
                    search_word(board, list(been_map), r, c-1, letters, letter_index+1)
                )


        if len(word) == 0:
            return True
        change_to_2d_matrix(board)
        #print board
        letters = [letter for letter in word]
        start_points = find_start_points(board, letters[0])
        #print "start points: %s" % start_points
        for start_point in start_points:
            if search_word(board, [], start_point[0], start_point[1], letters, 0) is True:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    board = ["ABCE","SFES","ADEE"]
    word = "ABCESEEEFS"
    print s.exist(board, word)


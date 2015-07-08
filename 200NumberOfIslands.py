# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
200: Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3

=== Comments by Dabay===
遍历每个点，如果是1，就把它设为x，然后往四个方向递归绵延设置x。同时计数器+1.
'''

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == "1":
                    self.DFS_spread(grid, i, j)
                    res += 1
        return res

    def DFS_spread(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return
        if grid[i][j] == "1":
            grid[i][j] = "x"
            self.DFS_spread(grid, i-1, j)
            self.DFS_spread(grid, i, j-1)
            self.DFS_spread(grid, i+1, j)
            self.DFS_spread(grid, i, j+1)


def main():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    sol = Solution()
    print sol.numIslands(grid)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
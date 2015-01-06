# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/dungeon-game/

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K)   -3      3
-5      -10     1
10      30      -5(P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) == 0:
            return 0

        row_count = len(dungeon)
        column_count = len(dungeon[0])

        helper_dungeon = []
        for r in xrange(row_count):
            row = []
            for c in xrange(column_count):
                row.append(0)
            helper_dungeon.append(row)

        if dungeon[-1][-1] >= 0:
            helper_dungeon[-1][-1] = 1
        else:
            helper_dungeon[-1][-1] = 1 - dungeon[-1][-1]

        for r in xrange(row_count-2, -1, -1):
            if dungeon[r][column_count-1] >= helper_dungeon[r+1][column_count-1] - 1:
                helper_dungeon[r][column_count-1] = 1
            else:
                helper_dungeon[r][column_count-1] = helper_dungeon[r+1][column_count-1] - dungeon[r][column_count-1]

        for c in xrange(column_count-2, -1, -1):
            if dungeon[row_count-1][c] >= helper_dungeon[row_count-1][c+1] - 1:
                helper_dungeon[row_count-1][c] = 1
            else:
                helper_dungeon[row_count-1][c] = helper_dungeon[row_count-1][c+1] - dungeon[row_count-1][c]

        for r in xrange(row_count-2, -1, -1):
            for c in xrange(column_count-2, -1, -1):
                min_cost = min(helper_dungeon[r+1][c], helper_dungeon[r][c+1])
                if dungeon[r][c] >= min_cost - 1:
                    helper_dungeon[r][c] = 1
                else:
                    helper_dungeon[r][c] = min_cost - dungeon[r][c]
        return helper_dungeon[0][0]


def main():
    dungeon = [
        [-2,-3,3],
        [-5,-10,1],
        [10,30,-5]
    ]
    s = Solution()
    print s.calculateMinimumHP(dungeon)


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)
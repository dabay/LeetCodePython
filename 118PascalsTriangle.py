# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

118: Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


===Comments by Dabay===
一级一级的生成。
'''

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        while numRows > 2:
            last_row = res[-1]
            new_row = [1]
            for i in xrange(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row.append(1)
            res.append(new_row)
            numRows -= 1
        return res



def main():
    sol = Solution()
    print sol.generate(5)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

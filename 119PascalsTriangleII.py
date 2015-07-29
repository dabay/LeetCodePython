# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

119: Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?

===Comments by Dabay===
一级一级的生成。
'''

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1,1]
        while rowIndex > 1:
            for i in xrange(len(res)-1):
                res[i] = res[i] + res[i+1]
            res.insert(0, 1)
            rowIndex -= 1
        return res


def main():
    sol = Solution()
    print sol.getRow(5)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

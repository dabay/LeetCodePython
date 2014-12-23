# -*- coding: utf8 -*-
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution:
    # @return an integer
    def numTrees(self, n):
        #@1  ->  1
        #@2  ->  2
        #@3  ->  5:  @2 + @2 + @1*@1
        #@4  ->  14:  @3 + @3 + @1*@2 + @2*@1
        num = {}
        num[1] = 1
        num[2] = 2

        for i in xrange(3, n+1):
            num[i] = 0
            for j in xrange(1, i-1):
                num[i] = num[i] + num[i-1-j]*num[j]
                #num[n-2]*num[1] + ... + num[1]*num[n-2]
            num[i] = num[i] + num[i-1]*2
        return num[n]

if __name__ == "__main__":
    s = Solution()
    print s.numTrees(4)

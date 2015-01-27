# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

72: Edit Distance
https://oj.leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

===Comments by Dabay===
使用DP。
https://web.stanford.edu/class/cs124/lec/med.pdf

For two strings:
• X of length n
• Y of length m
We define D(i,j)
• the edit distance between X[1..i] and!Y[1..j]
    • i.e., the first i characters of X and the first j characters of Y
• The edit distance between X and Y is thus D(n,m)

Initialization
D(i,0) = i
D(0,j) = j
Recurrence Relation:
    For each i = 1…M
        For each j = 1…N
            D(i-1,j) + 1
            D(i,j)= min
                        D(i-1,j) + 1
                        D(i,j-1) + 1
                        D(i-1,j-1) +
                            1; if X(i) ≠ Y(j)
                            0; if X(i) = Y(j)
Termination:
D(M,N) is distance
'''
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        res = []
        row = [x for x in xrange(n+1)]
        res.append(row)
        for i in xrange(1, m+1):
            row = [i] + [0 for _ in xrange(1, n+1)]
            res.append(row)

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                x = min(res[i-1][j]+1, res[i][j-1]+1)
                y = res[i-1][j-1]
                if word1[i-1]!=word2[j-1]:
                    y += 1
                res[i][j] = min(x, y)
        return res[-1][-1]


def main():
    sol = Solution()
    word1 = "a"
    word2 = "b"
    print sol.minDistance(word1, word2)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
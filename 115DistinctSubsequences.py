# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

115: Distinct Subsequences
https://oj.leetcode.com/problems/distinct-subsequences/

Given a string S and a string T, count the number of distinct subsequences of T in S.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

===Comments by Dabay===
动态规划。
首先要想好，那个作为横坐标那个作为纵坐标。这里选择子串T为横坐标，母串S为纵坐标。
然后想好递推关系，
    如果字符不相同，匹配的次数不增加
    如果相同，就需要加上子母串都不包含这个字符的时候所匹配的次数，即res[i-1][j-1]
'''

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        res = []
        row = [1] + [0 for _ in T]
        res.append(row)
        for _ in S:
            res.append([1] + [0 for _ in T])

        for i in xrange(1, len(S)+1):
            for j in xrange(1, len(T)+1):
                if S[i-1] == T[j-1]:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
                else:
                    res[i][j] = res[i-1][j]

        return res[-1][-1]


def main():
    sol = Solution()
    S = "rabbbit"
    T = "rabbit"
    print sol.numDistinct(S, T)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

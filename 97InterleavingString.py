# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

97: Interleaving String
https://oj.leetcode.com/problems/interleaving-string/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
For example,
Given:
s1 = "aabcc",
s2 = "dbbca",
When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

===Comments by Dabay===
开始准备记录一个在s1和s2中移动的指针组合，匹配每一个s3中字符之后，更新这个指针组合。
但是当s1和s2为 "aaaaaaaaaa"，s3 = "aaaaaaaaaaaaaaaaaaaa"的时候，这个组合数量达到了18w+。太耗内存了。

递归会好一些，但是相信时间复杂度还是比较高。

最后还得用动态规划。
判断的res[i][j]的时候，即判断 s3中前i+j个字符是否 与 s1中前i个与s2中前j个字符 匹配（这里i代表s1中第i个，j代表s2中第j个）：
两种情况设置为True:
    1. s3中第i+j个字符与s1中第i个字符匹配，而且s3中前i+j-1个字符 与 s1中前i-1个字符和s2中前j个字符 匹配
    2. s3中第i+j个字符与s2中第j个字符匹配，而且s3中前i+j-1个字符 与 s1中前i个字符和s2中前j-1个字符 匹配
'''

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        res = []
        row = [True] + [False for _ in s1]
        res.append(row)
        for i in xrange(1, len(s1)+1):
            if s3[i-1] == s1[i-1] and res[0][i-1] is True:
                res[0][i] = True

        for j in xrange(1, len(s2)+1):
            row = []
            if s3[j-1] == s2[j-1] and res[j-1][0] is True:
                row.append(True)
            else:
                row.append(False)
            row += [False for _ in s1]
            res.append(row)
            for i in xrange(1, len(s1)+1):
                if (s3[j+i-1] == s1[i-1] and res[j][i-1]) or (s3[j+i-1] == s2[j-1] and res[j-1][i]):
                    res[j][i] = True

        return res[-1][-1]


def main():
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print sol.isInterleave(s1, s2, s3)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)


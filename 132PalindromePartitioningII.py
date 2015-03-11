# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

132: Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

=== Comments by Dabay===
以下摘自网络：http://www.cnblogs.com/springfor/p/3891896.html
这道题需要用动态规划做，如果用I的DFS的方法做会TLE。
 首先设置dp变量 cuts[len+1]。cuts[i]表示从第i位置到第len位置（包含，即[i, len])的切割数（第len位置为空）。
 初始时，是len-i。比如给的例子aab，cuts[0]=3，就是最坏情况每一个字符都得切割：a|a|b|' '。cuts[1] = 2, 即从i=1位置开始，a|b|' '。
 cuts[2] = 1 b|' '。cuts[3]=0,即第len位置，为空字符，不需要切割。
 上面的这个cuts数组是用来帮助算最小cuts的。
 还需要一个dp二维数组matrixs[i][j]表示字符串[i,j]从第i个位置（包含）到第j个位置（包含） 是否是回文。
 如何判断字符串[i,j]是不是回文？
 1. matrixs[i+1][j-1]是回文且 s.charAt(i) == s.charAt(j)。
 2. i==j（i，j是用一个字符）
 3. j=i+1（i，j相邻）且s.charAt(i) == s.charAt(j)
 当字符串[i,j]是回文后，说明从第i个位置到字符串第len位置的最小cut数可以被更新了，
 那么就是从j+1位置开始到第len位置的最小cut数加上[i,j]|[j+1,len - 1]中间的这一cut。
 即，Math.min(cuts[i], cuts[j+1]+1)
 最后返回cuts[0]-1。把多余加的那个对于第len位置的切割去掉，即为最终结果。
'''

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        cuts = [len(s)-i for i in xrange(len(s)+1)]
        matrix = [[False for _ in xrange(len(s))] for _ in xrange(len(s)+1)]
        for i in xrange(len(s)-1, -1, -1):
            for j in xrange(i, len(s)):
                if (matrix[i+1][j-1] and s[i] == s[j]) or (j == i and s[i] == s[j]) or (j == i + 1 and s[i] == s[j]):
                    matrix[i][j] = True
                    cuts[i] = min(cuts[i], cuts[j+1]+1)
        return cuts[0]-1


def main():
    sol = Solution()
    print sol.minCut("aab")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
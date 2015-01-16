# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/regular-expression-matching/

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

===Comments by Dabay===
这道题应该用动态规划的做法。我只想说，头大！

建立一个二维数组，第一维是s为基础，第二维是p为基础。（顺序很重要）
初始化res[0]，长度比p多1，即多第一个true。同时考虑p中开始的几个偶数为是*的情况，初始化相应的true。其他为false。

然后每次放一个s中元素进来，尝试匹配整个p。

三种情况：（每次更新的是res[i+1][j+1]）
    如果p[j]不是.和*，即是一般比较，同时观察res[i][j]。
    如果p[j]是.，无需比较，根据res[i][j]的值即可。
    如果p[j]是*，
        考虑匹配零次的情况：判断res[i+1][j-1]是否为true
        考虑匹配一次的情况：判断res[i+1][j]是否为true
        考虑匹配多次的情况：判断字符是否相符，同时判断res[i][j+1]
'''
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        res = []
        defaultRow = [False] + [False for _ in p]
        res.append(list(defaultRow))
        res[0][0] = True
        for x in xrange(len(p)):
            if p[x] == '*':
                res[0][x+1] = res[0][x-1]

        for i in xrange(len(s)):
            res.append(list(defaultRow))
            for j in xrange(len(p)):
                if p[j] != '*':
                    if (s[i] == p[j] or p[j] == '.') and res[i][j]:
                        res[i+1][j+1] = True
                elif p[j] == '.':
                    if res[i][j]:
                        res[i+1][j+1] = True
                else: # *
                    #匹配0次
                    if res[i+1][j-1]:
                        res[i+1][j+1] = True
                    #匹配1次
                    if res[i+1][j]:
                        res[i+1][j+1] = True
                    #匹配多次
                    if (s[i] == p[j-1] or p[j-1] == '.') and res[i][j+1]:
                        res[i+1][j+1] = True
        return res[-1][-1]


def main():
    sol = Solution()
    s = "aab"
    p = "c*a*b"
    print sol.isMatch(s, p)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
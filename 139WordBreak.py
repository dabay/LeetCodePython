# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

139: Word Break
https://oj.leetcode.com/problems/word-break/

Given a string s and a dictionary of words dict,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".

=== Comments by Dabay===
一维动态规划。
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return False
        possibility = [True] + [False for _ in s]

        for i in xrange(len(s)):
            for j in xrange(i+1):
                if possibility[j] is True and s[j:i+1] in dict:
                    possibility[i+1] = True

        return possibility[-1]


def main():
    s = Solution()
    string = "leetcode"
    dict = ["leet","code"]
    print s.wordBreak(string, dict)


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)
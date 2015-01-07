# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/word-break/

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return False

        possible = [False for _ in xrange(len(s))]
        if s[0] in dict:
            possible[0] = True
        for i in xrange(1, len(s)):
            if s[:i+1] in dict:
                possible[i] = True
                continue
            for j in xrange(i+1):
                if possible[j] == False:
                    continue
                if s[j+1:i+1] in dict:
                    possible[i] = True
                    break
        return possible[-1]



def main():
    s = Solution()
    string = "aaaaaaa"
    dict = ["aaaa","aa"]
    #dict = ["a"]
    print s.wordBreak(string, dict)


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)
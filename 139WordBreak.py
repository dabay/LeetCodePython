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

        for d in dict:


        result = False
        max_word_length = max([len(word) for word in dict])
        #print max_word_length
        for i in xrange(max_word_length, 0, -1):
            if s[:i] in dict:
                if i == len(s):
                    return True
                else:
                    result = result | self.wordBreak(s[i:], dict)
            if result is True:
                break
        return result


def main():
    s = Solution()
    string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    #dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    dict = ["a"]
    print s.wordBreak(string, dict)


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

140: Word Break II
https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence
where each word is a valid dictionary word.
Return all such possible sentences.
For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].

=== Comments by Dabay===
https://stupidcodergoodluck.wordpress.com/2013/11/16/leetcode-word-break-ii/

'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return [""]
        res = []
        if self.can_break_dp(s, dict):
            self.word_break_dfs(s, dict, [], res)
        return res

    def word_break_dfs(self, s, dict, tmp, res):
        if len(s) == 0:
            res.append(' '.join(tmp))
            return
        for i in xrange(1, len(s)+1):
            sliced_string = s[:i]
            if sliced_string in dict:
                tmp.append(sliced_string)
                self.word_break_dfs(s[i:], dict, tmp, res)
                tmp.pop(-1)

    def can_break_dp(self, s, dict):
        possibility = [True] + [False for _ in s]
        for i in xrange(len(s)):
            for j in xrange(i+1):
                if possibility[j] is True and s[j:i+1] in dict:
                    possibility[i+1] = True
        return possibility[-1]


def main():
    sol = Solution()
    s = "aaa"
    dict = ["a","aa"]
    print sol.wordBreak(s, dict)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
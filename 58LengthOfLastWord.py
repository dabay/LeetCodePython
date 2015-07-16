# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

58: Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

===Comments by Dabay===
获得最后一个单词，返回其长度。
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        last_word = s.rstrip().split(" ")[-1]
        return len(last_word)


def main():
    sol = Solution()
    print sol.lengthOfLastWord("Hello World")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



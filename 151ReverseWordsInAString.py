# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/reverse-words-in-a-string/

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split(" ")
        result = ""
        while len(words)>=1:
            word = words.pop(-1)
            if word != "":
                result = result + " " + word
        return result.lstrip(" ")

def main():
    s = Solution()
    string = "a"
    string = "  the sky is blue"
    print s.reverseWords(string)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    end = time.clock()
    print "%s sec" % (end - start)
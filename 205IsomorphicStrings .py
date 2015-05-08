# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

205: Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

=== Comments by Dabay===
把单词转化成模板，然后判断两个模板是否一样。
'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        template1 = []
        template2 = []

        i = 0
        h = {}
        for c in s:
            if c not in h:
                h[c] = i
                i += 1
            template1.append(h[c])

        i = 0
        h = {}
        for c in t:
            if c not in h:
                h[c] = i
                i += 1
            template2.append(h[c])

        return template1 == template2


def main():
    sol = Solution()
    print sol.isIsomorphic("egg", "add")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
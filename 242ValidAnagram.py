# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
242: Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

=== Comments by Dabay===
使用hash table.
'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if c not in d.keys():
                return False
            else:
                if d[c] == 0:
                    return False
                else:
                    d[c] -= 1
        return True


def main():
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print sol.isAnagram(s, t)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
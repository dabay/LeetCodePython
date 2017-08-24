# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
290. Word Pattern
https://leetcode.com/problems/word-pattern/description/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

=== Comments by Dabay===
先把str按空格分解放在数组里面,维护一个hash表来作为比对,key是pattern,value是str中的词。
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        array = str.split()
        h = {};
        if len(pattern) != len(array):
            return False
        for i in xrange(len(pattern)):
            if (h.has_key(pattern[i])):
                if (h[pattern[i]] != array[i]):
                    return False
            else:
                if (array[i] not in h.values()):
                    h[pattern[i]] = array[i]
                else:
                    return False
        return True


def main():
    sol = Solution()
    pattern = "abba";
    str = "dog dog dog dog";
    print sol.wordPattern(pattern, str)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
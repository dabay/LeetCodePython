# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

49: Anagrams
https://leetcode.com/problems/anagrams/

Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.

=== Comments by Dabay===
http://blog.csdn.net/linhuanmars/article/details/21664747
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        hash_table = {}
        for str in strs:
            l = list(str)
            l.sort()
            sorted_str = ''.join(l)
            if sorted_str in hash_table:
                hash_table[sorted_str].append(str)
            else:
                hash_table[sorted_str] = [str]
        res = []
        for sorted_str in hash_table:
            if len(hash_table[sorted_str]) > 1:
                res.extend(hash_table[sorted_str])
        return res


def main():
    sol = Solution()
    strs = ["ab", "ba", "abc", "cba", "z"]
    print sol.anagrams(strs)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
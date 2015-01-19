# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/longest-common-prefix/
14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
===Comments by Dabay===
注意边界条件，如果strs为空，直接返回空字符串。

初始化共同前缀为空字符串。
如果一个字符出现在每个字符的相应位置就把这个字符加到共同前缀中。
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        common_pre = ""
        i = 0
        while True:
            to_compare = ""
            for s in strs:
                if i >= len(s):
                    return common_pre
                if to_compare == "":
                    to_compare = s[i]
                    continue
                if s[i] != to_compare:
                    return common_pre
            else:
                common_pre = common_pre + to_compare
            i = i + 1


def main():
    s = Solution()
    strs = ["abcdef", "abc", "abcd"]
    print s.longestCommonPrefix(strs)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



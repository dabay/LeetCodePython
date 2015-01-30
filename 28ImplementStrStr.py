# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

28: Implement strStr()
https://oj.leetcode.com/problems/implement-strstr/

Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

===Comments by Dabay===
在长字符串中找子串，当然是KMP算法。既然是三人研究出来的算法，肯定不简单。空了再来研究研究吧。
这里给的是直观的解法，遍历长字符串的时候，开始和短字符串一个一个字符进行比较，如果都比较完了，说明找到了。
如果遍历完了，还没有返回的话，说明没有找到，返回-1。
'''

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        i = 0
        while i < len(haystack) - len(needle) + 1:
            m,n = i,0
            while n < len(needle) and haystack[m] == needle[n]:
                m += 1
                n += 1
            if n == len(needle):
                return i
            i += 1
        else:
            return -1


def main():
    sol = Solution()
    haystack = "ahi"
    needle = "hi"
    print sol.strStr(haystack, needle)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

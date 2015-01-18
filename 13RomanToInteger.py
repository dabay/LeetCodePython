# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/roman-to-integer/
Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
===Comments by Dabay===
先google一下罗马数字的表示：
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000
主要问题是考虑一些4,40之类的表示。

可以从右往左，依次处理：
当遇到这个字母表示的数字比后一个小的时候，减去这个数；否则，累加。
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        if len(s) == 0:
            return 0
        value = 0
        for i in xrange(len(s)-1, -1, -1):
            if i < len(s)-1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                value = value - roman_dict[s[i]]
            else:
                value = value + roman_dict[s[i]]
        return value


def main():
    s = Solution()
    print s.romanToInt("MCMXCIX")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



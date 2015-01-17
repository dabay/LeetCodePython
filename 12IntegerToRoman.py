# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/integer-to-roman/
Integer to Roman

Given an integer, convert it to a roman numeral.

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
主要问题是会有一些4,40之类的表示。
比如999的时候，因为900可以表示为CM，所以需要先生成CM，数字减少900为99；而不是减少500为499.
可以生成一个有序的键值表，每次减少最大的，直到剩下的数小于hash表中的最大数，把这个最大数删掉继续处理。
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        pairs = [
            (1000,"M"),
            (900,"CM"),
            (500,"D"),
            (400,"CD"),
            (100,"C"),
            (90,"XC"),
            (50,"L"),
            (40,"XL"),
            (10,"X"),
            (9,"IX"),
            (5,"V"),
            (4,"IV"),
            (1,"I")
        ]
        res = ""
        for (n, s) in pairs:
            while num >= n:
                res = res + s
                num = num - n
        return res


def main():
    s = Solution()
    print s.intToRoman(6)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



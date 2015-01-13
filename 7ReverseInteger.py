# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/reverse-integer/

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of
1000000003 overflows. How should you handle such cases?
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    # @return an integer
    def reverse(self, x):
        int_str = str(x)
        new_int = 0
        for i in range(len(int_str)-1, -1, -1):
            if int_str[i] in "0123456789":
                new_int = new_int * 10 + int(int_str[i])
                continue
            if int_str[i] == "-":
                new_int = new_int * -1
                break
        if new_int > 2147483647 or new_int < -2147483647:
            new_int = 0
        return new_int
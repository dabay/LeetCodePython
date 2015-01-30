# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

29: Divide Two Integers
https://oj.leetcode.com/problems/divide-two-integers/

Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.

===Comments by Dabay===

先确定符号。

做除法式子：
一个字符串保存商，一个字符串保存余数。
计算每一位商的时候，用余数来减除数，如果剩下的数大于0，商就加1。

最后返回的时候，考虑题目中提到的overflow。（个人感觉这个要求没什么意义）
'''

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            quotient = "-"
        else:
            quotient = ""
        dividend = abs(dividend)
        divisor = abs(divisor)

        dividend = str(dividend)
        i = 0
        remainder = ""
        while i < len(dividend):
            remainder = int(str(remainder) + dividend[i])
            quot = 0
            while remainder >= divisor:
                remainder -= divisor
                quot += 1
            quotient += str(quot)
            i += 1

        if int(quotient) > 2147483647:
            return 2147483647
        elif int(quotient) < -2147483648:
            return 2147483648
        else:
            return int(quotient)


def main():
    sol = Solution()
    print sol.divide(1, -1)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

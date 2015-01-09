# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

我好烦这样的题啊，要把思路转化为bug free的代码好累...
'''

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        minus = (numerator < 0) ^ (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        div = numerator / denominator
        mod = numerator % denominator
        if mod == 0:
            if minus and div!=0:
                return "-" + str(div)
            else:
                return str(div)

        num_part = str(div)
        decimal_part = ""

        positions = []

        while True:
            n = mod * 10
            div = n / denominator
            mod = n % denominator
            if mod == 0:
                decimal_part = decimal_part + str(div)
                break
            if (div, mod) in positions:
                break
            decimal_part = decimal_part + str(div)
            positions.append((div, mod))

        if (div, mod) in positions:
            i = positions.index((div, mod))
            decimal_part = decimal_part[:i] + "(" + decimal_part[i:] + ")"

        if minus:
            return "-" + num_part + "." + decimal_part
        else:
            return num_part + "." + decimal_part



def main():
    s = Solution()
    print s.fractionToDecimal(-2147483648, 1)

if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

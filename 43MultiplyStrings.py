# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

43: Multiply Strings
https://leetcode.com/problems/multiply-strings/

Given two numbers represented as strings, return multiplication of the numbers as a string.
Note: The numbers can be arbitrarily large and are non-negative.

=== Comments by Dabay===
用小学学的乘法公式。
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        # if len(num1) < len(num2):
        #     num1, num2 = num2, num1
        res = ""
        for j in reversed(xrange(len(num2))):
            tmp = ""
            carry = 0
            for i in reversed(xrange(len(num1))):
                x = int(num1[i]) * int(num2[j]) + carry
                carry = x / 10
                x = x % 10
                tmp = str(x) + tmp
            if carry != 0:
                tmp = str(carry) + tmp
            res = self.num_add(res, tmp + "0" * (len(num2)-1-j))
        return res


    def num_add(self, num1, num2):
        if len(num1) > len(num2):
            num2 = num2.zfill(len(num1))
        else:
            num1 = num1.zfill(len(num2))
        res = ""
        carry = 0
        for i in reversed(xrange(len(num1))):
            x = int(num1[i]) + int(num2[i]) + carry
            if x >= 10:
                x -= 10
                carry = 1
            else:
                carry = 0
            res = str(x) + res
        if carry == 1:
            res = "1" + res
        return res


def main():
    sol = Solution()
    num1 = "999"
    num2 = "999"
    print sol.num_add(num1, num2)
    print sol.multiply(num1, num2)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
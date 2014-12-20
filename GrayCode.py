# -*- coding: utf8 -*-
'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

http://zh.wikipedia.org/wiki/%E6%A0%BC%E9%9B%B7%E7%A0%81
这个不了解的格雷码的编码规律是不行的吧..  -_-
'''
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        def generate_gray_list(n):
            if n == 1:
                return ["0", "1"]

            result = []
            l = generate_gray_list(n-1)
            for i in xrange(0, len(l)):
                result.append("0" + l[i])
            for i in xrange(len(l)-1, -1, -1):
                result.append("1" + l[i])
            return result


        def binary_string_to_decimal_number(string):
            v = 0
            factor = 1
            for i in xrange(-1, 0-len(string)-1, -1):
                if string[i] == "1":
                    v = v + factor
                factor = factor * 2
            return v

        if n == 0:
           return [0]

        result = []
        for s in generate_gray_list(n):
            result.append(binary_string_to_decimal_number(s))
        return result


if __name__ == "__main__":
    s = Solution()
    print s.grayCode(2)

# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

191: Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has
(also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
so the function should return 3.

=== Comments by Dabay===
转换整形为二进制字符串，然后处理字符串，数其中1的个数。

>>> '{0:08b}'.format(6)
00000110
Just to explain the parts of the formatting string:

{} places a variable into a string
0 takes the variable at argument position 0
: adds formatting options for this variable (otherwise it would represent decimal 6)
08 formats the number to eight digits zero-padded on the left
b converts the number to its binary representation

'''

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        bin_str = '{0:032b}'.format(n)
        count = 0
        for c in bin_str:
            if c == '1':
                count +=1
        return count


def main():
    sol = Solution()
    n = 11
    print sol.hammingWeight(n)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

190: Reverse Bits
https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
Related problem: Reverse Integer

=== Comments by Dabay===
字符串的操作。注意前面补0。
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_str = "{0:b}".format(n)
        bin_str = bin_str.zfill(32)
        bin_str_list = list(bin_str)
        bin_str_list.reverse()
        new_bin_str = ''.join(bin_str_list)
        return int(new_bin_str, 2)


def main():
    sol = Solution()
    print sol.reverseBits(1)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

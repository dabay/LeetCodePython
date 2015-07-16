# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

67: Add Binary
https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".

===Comments by Dabay===
按位加，注意处理进位。
'''

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        overflow = 0
        max_length = max(len(a), len(b))
        new_a = a.zfill(max_length + 1)
        new_b = b.zfill(max_length + 1)
        res = ["0" for i in xrange(max_length+1)]
        for i in reversed(xrange(len(new_a))):
            if int(new_a[i]) + int(new_b[i]) + overflow >= 2:
                res[i] = str(int(new_a[i]) + int(new_b[i]) + overflow - 2)
                overflow = 1
            else:
                res[i] = str(int(new_a[i]) + int(new_b[i]) + overflow)
                overflow = 0
        result = "".join(res).lstrip("0")
        return [result,"0"][result==""]


def main():
    sol = Solution()
    print sol.addBinary("11", "1")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

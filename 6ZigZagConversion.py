# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

===Comments by Dabay===
用nRows个数组来接受每一个字符。

当nRows等于1时，直接返回s。

当nRows大于等于2时，定义nRows个数组，
2*nRows-2 为一个循环。从第一行到最后一行，再从倒数第二行回到第二行。
用模来确定位置，
    当小于等于nRows-1的时候，直接放到模对应的数组里面
    当大于nRows-1的时候，这里是数学题了：
        mod-(nRows-1)为应该往上数的行数，最后一行的标号为nRow-1，所以这个行标应该是：(nRow-1)-(mod-(nRows-1))=2*nRows-mod-2
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        array2d = [[] for _ in xrange(nRows)]
        for i in xrange(len(s)):
            mod = i % (2*nRows-2)
            if mod <= nRows-1:
                array2d[mod].append(s[i])
            else:
                x = 2*nRows - mod -2
                array2d[x].append(s[i])
        val = ""
        for row in array2d:
            for v in row:
                val = val + v
        return val


def main():
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
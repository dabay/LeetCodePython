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

===Comments by Dabay===
先简单是否是负数，用minus来记录。
然后把字符串reverse。
最后检查是否越界。
'''
class Solution:
    # @return an integer
    def reverse(self, x):
        if len(x) <= 1:
            return x
        x = str(x)
        minus = False
        if x[0] == '-':
            minus = True
            x = x[1:]
        stack = []
        for n in x:
            stack.append(n)
        ret = ""
        while len(stack) > 0:
            ret = ret + stack.pop()
        ret = int(ret)
        if minus:
            ret = ret * -1
            if ret < -2147483647:
                return 0
        else:
            if ret > 2147483647:
                return 0
        return ret


def main():
    s = Solution()
    print s.reverse("-2147483648")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
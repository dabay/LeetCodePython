# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

===Comments by Dabay===
这里说的不用额外的空间，实际是指不用堆上的空间（程序外使用的内存空间）。
所以，变量这种使用程序栈的空间是可以的。

从两边往中间比较。用除以10的某次方的商，在取模可以得到需要比较的数。
'''
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div = div * 10

        div_left = div
        div_right = 1

        while div_left > div_right:
            left = x / div_left % 10
            right = x / div_right % 10
            if left != right:
                return False
            div_left = div_left / 10
            div_right = div_right * 10

        return True


def main():
    s = Solution()
    print s.isPalindrome(101232101)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

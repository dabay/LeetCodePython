# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

66: Plus One
https://leetcode.com/problems/plus-one/

Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

===Comments by Dabay===
从最后一个数字开始+1，如果进位就继续。
'''

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        overflow = True
        index = len(digits) - 1
        while index >= 0:
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                overflow = False
                break
            index -= 1
        if overflow:
            digits.insert(0, 1)
        return digits


def main():
    sol = Solution()
    print sol.plusOne([0])


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



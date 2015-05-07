# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

202: Happy Number
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

=== Comments by Dabay===
把每次的结果记录下来，如果重复了，就不happy了。
'''

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        s = str(n)
        results = []
        while True:
            num_list = [number for number in s]
            result = 0
            print num_list
            for number in num_list:
                result += int(number) ** 2
            if result == 1:
                return True
            if result in results:
                return False
            results.append(result)
            s = str(result)


def main():
    sol = Solution()
    print sol.isHappy(2)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
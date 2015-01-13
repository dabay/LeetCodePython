# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/string-to-integer-atoi/

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character
is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many
numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and
have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of
representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

===Comments by Dabay===
主要就是处理各种情况：
先把两边的引号和空格去掉。
然后确定符号。
接着读数字。
最后判断越界。
'''
class Solution:
    # @return an integer
    def atoi(self, str):
        str_new = str.strip("'").strip('"').strip()
        if str_new == "":
            return 0

        result = 0
        positive = True
        start_flag = False
        for i in xrange(len(str_new)):
            if start_flag is False:
                if str_new[i] == "-":
                    positive = False
                    start_flag = True
                    continue
                if str_new[i] == "+":
                    start_flag = True
                    continue
            if str_new[i] in "0123456789":
                start_flag = True
                result = result * 10 + int(str_new[i])
            else:
                break

        if not positive:
            result = result * -1
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648

        return result


def main():
    s = Solution()
    print s.atoi(" -00012a3 +2")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

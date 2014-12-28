# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/excel-sheet-column-number/

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        dict = {}
        dict["A"] = 1
        dict["B"] = 2
        dict["C"] = 3
        dict["D"] = 4
        dict["E"] = 5
        dict["F"] = 6
        dict["G"] = 7
        dict["H"] = 8
        dict["I"] = 9
        dict["J"] = 10
        dict["K"] = 11
        dict["L"] = 12
        dict["M"] = 13
        dict["N"] = 14
        dict["O"] = 15
        dict["P"] = 16
        dict["Q"] = 17
        dict["R"] = 18
        dict["S"] = 19
        dict["T"] = 20
        dict["U"] = 21
        dict["V"] = 22
        dict["W"] = 23
        dict["X"] = 24
        dict["Y"] = 25
        dict["Z"] = 26

        result = 0
        for c in s:
            result = result*26 + dict[c]
        return result

if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber("ABA")
    # import string
    # i = 1
    # for l in string.ascii_letters[:26]:
    #     print 'dict["%s"] = %s' % (str(l).upper(), i)
    #     i = i + 1
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

17: Letter Combinations of a Phone Number
https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

===Comments by Dabay===
比较典型的递归调用。
每次消化掉一个字数，把其对应的字母和已有的字符串做笛卡尔乘积。
'''

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        def letterCombinations2(digits, strings, d):
            if len(digits) == 0:
                return strings
            letters = d[digits[0]]
            new_strings = []
            for letter in letters:
                for i in xrange(len(strings)):
                    new_strings.append(strings[i] + letter)
            return letterCombinations2(digits[1:], new_strings, d)

        d = {}
        d["0"] = d["1"] = ""
        d["2"] = "abc"
        d["3"] = "def"
        d["4"] = "ghi"
        d["5"] = "jkl"
        d["6"] = "mno"
        d["7"] = "pqrs"
        d["8"] = "tuv"
        d["9"] = "wxyz"
        return letterCombinations2(digits, [""], d)


def main():
    sol = Solution()
    print sol.letterCombinations("23")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
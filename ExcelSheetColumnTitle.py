# -*- coding: utf8 -*-
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''

class Solution:
    # @return a string
    def convertToTitle(self, num):
        # import string
        # letters = string.uppercase[:26]
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        result = ""
        while num >= 26:
            mod = num % 26
            num = num / 26
            if mod == 0:
                num = num - 1
                result = letters[-1] + result
            else:
                result = letters[mod-1] + result
        if num != 0:
            result = letters[num-1] + result
        return result

if __name__ == "__main__":
    s = Solution()
    print s.convertToTitle(26)
    # 52: "AZ"
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

125: Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.

===Comments by Dabay===
效率比较低下，属于后30%。
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        letters = "abcdefghijklmnopqrstuvwxyz1234567890"
        new_string_list = []
        for c in s.lower():
            if c in letters:
                new_string_list.append(c)
        for i in xrange(len(new_string_list)/2):
            if new_string_list[i] != new_string_list[len(new_string_list)-1-i]:
                return False
        else:
            return True


def main():
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print sol.isPalindrome(s)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

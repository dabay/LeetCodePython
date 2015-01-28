# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

87: Scramble String
https://oj.leetcode.com/problems/scramble-string/

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

===Comments by Dabay===
看题意不是很明白，还以为只是从中间断，结果是可以从任意位置断。
断的时候，考虑两种情况，即断开的左右两边是否交换了位置。
每次先判断isScramble的时候，先判断是否有相同的字母。用这个剪枝之后就可以过OJ了。
有DP的解法，还没有研究。
'''

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        def same_letters(s1, s2):
            letters = list(s1)
            for c in s2:
                if c not in letters:
                    return False
                else:
                    letters.remove(c)
            return len(letters) == 0

        if same_letters(s1, s2) is False:
            return False
        if len(s1) == 1:
            return s1 == s2
        for i in xrange(1, len(s1)):
            s1_left = s1[:i]
            s1_right = s1[i:]

            s2_left = s2[:i]
            s2_right = s2[i:]
            if self.isScramble(s1_left, s2_left) and self.isScramble(s1_right, s2_right):
                return True

            s2_left = s2[:len(s2)-i]
            s2_right = s2[len(s2)-i:]
            if self.isScramble(s1_left, s2_right) and self.isScramble(s1_right, s2_left):
                return True
        else:
            return False


def main():
    sol = Solution()
    s1 = "abcdefghijklmnopq"
    s2 = "efghijklmnopqcadb"
    print sol.isScramble(s1, s2)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

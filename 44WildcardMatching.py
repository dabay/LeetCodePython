# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

44：Wildcard Matching
https://oj.leetcode.com/problems/wildcard-matching/

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

===Comments by Dabay===
使用动态规划的做法.
先想象在s和p的前面都加一个空格，以s为外循环，p为内循环。
先初始化第一组数据，第一个“空”匹配“空”，所以第一个为True。然后看如果后面如果是*就继续设置为True。

进入循环之后，判断根据p中的字符
    - 如果是？*以外的字符，就判断这个字符和s中对应的字符是否一致，而且s中到上一个字符和p中到上一次字符匹配，设True
    - 如果是？，如果s中到上一个字符和p中到上一个字符匹配，设True
    - 如果是*，满足下面的情况，就设True
        - （匹配0次）s中到这个字符和p到上两个字符匹配
        - （匹配1次）s中到这个字符和p到上一个字符匹配
        - （匹配n次）s中到上一个字符和p到这个字符匹配
'''

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        def quick_test(s, p):
            num_of_star = 0
            for x in p:
                if x == "*":
                    num_of_star = num_of_star + 1
            return len(s) >= len(p)-num_of_star

        if quick_test(s, p) is False:
            return False
        default_row = [False] + [False for _ in p]
        current_row = list(default_row)
        current_row[0] = True
        for j in xrange(len(p)):
            if p[j] == "*":
                current_row[j+1] = True
            else:
                break
        previous_row = current_row
        for i in xrange(len(s)):
            current_row = list(default_row)
            for j in xrange(len(p)):
                if p[j] == "?":
                    if previous_row[j]:
                        current_row[j+1] = True
                elif p[j] == "*":
                    if current_row[j] or previous_row[j] or previous_row[j+1]:
                        current_row[j+1] = True
                else:
                    if p[j] == s[i] and previous_row[j]:
                        current_row[j+1] = True
            previous_row = current_row
        return previous_row[-1]


def main():
    sol = Solution()
    s = "ac"
    p = "ab*"
    print sol.isMatch(s, p)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)



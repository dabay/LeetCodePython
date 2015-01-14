# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/regular-expression-matching/

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

===Comments by Dabay===
自我感觉很解得很垃圾啊。如果不是把p做了压缩还过不了online judge。

当s和p都是空的时候，匹配成功。
如果s为空，p不为空，检查p的偶数为是不是都是*。

如果s和p都不为空，头一个字母
    如果不匹配，
        不带*，False
        带*，递归p[2:]
    如果匹配，
        不带*，递归s[1:],p[1:]
        带*，考虑匹配0到最远端的情况，分别递归s[i:],p[2:]
'''
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def compress(p):
            i = 0
            while i < len(p)-3:
                if p[i+1] != '*':
                    i = i + 1
                    continue
                if p[i+3] == '*':
                    if p[i] == "." or p[i+2] == ".":
                        p = p[:i] + ".*" + p[i+4:]
                        continue
                    elif p[i] == p[i+2]:
                        p = p[:i] + p[i+2:]
                        continue
                i = i + 2
            return p

        def isMatch2(s, p):
            if len(s) == 0:
                if len(p) == 0:
                    return True
                if len(p) % 2 == 0:
                    i = 1
                    while i < len(p):
                        if p[i] != "*":
                            return False
                        i = i + 2
                    else:
                        return True
                else:
                    return False
            if len(s) > 0 and len(p) == 0:
                return False

            match_char = p[0]
            multi = False
            if len(p) > 1:
                if p[1] == "*":
                    multi = True

            if match_char != s[0] and match_char != ".":
                if multi:
                    return isMatch2(s, p[2:])
                else:
                    return False

            if multi is False:
                return isMatch2(s[1:], p[1:])
            else:
                result = False
                i = 0
                result = isMatch2(s, p[2:])
                while i < len(s):
                    if result == True:
                        return result
                    if (s[i] == match_char or match_char == "."):
                        result = isMatch2(s[i+1:], p[2:])
                    else:
                        break
                    i = i + 1
                return result

        return isMatch2(s, compress(p))


def main():
    s = Solution()
    print s.isMatch("aa", "a*")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
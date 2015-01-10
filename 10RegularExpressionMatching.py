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

不知道大家得用多长时间来解决这个题呀？这个题放在面试中，不得急死人啊...
'''
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def compress(p):
            i = 0
            while i < len(p)-3:
                if (p[i] == p[i+2] or p[i] == "." or p[i+2] == ".") and (p[i+1] == "*" and p[i+3] == "*"):
                    contain_dot = False
                    if p[i] == "." or p[i+2] == ".":
                        contain_dot = True

                    if contain_dot:
                        p = p[:i] + ".*" + p[i+4:]
                    else:
                        p = p[:i] + p[i+2:]
                else:
                    i = i + 1
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
    print s.isMatch("a", "ab*")


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
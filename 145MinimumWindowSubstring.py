# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

145: Minimum Window Substring
https://oj.leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".
If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

===Comments by Dabay===

记录每一个关键词出现的位置.
先把满足条件的字符串找出来，然后压缩这个字符串。

思路比较清晰，代码乱。
'''

class Solution:
    # @return a string
    def minWindow(self, S, T):
        def found_all(keyword_dict_string, keyword_dict):
            for keyword in keyword_dict:
                if keyword not in keyword_dict_string or keyword_dict_string[keyword] < keyword_dict[keyword]:
                    return False
            return True

        def shrink_left(s, e, keyword_dict_string, keyword_dict, keyword_postions, string):
            while s < e:
                keyword = string[keyword_postions[s]]
                if keyword_dict_string[keyword]-1 < keyword_dict[keyword]:
                    break
                else:
                    keyword_dict_string[keyword] -= 1
                    s += 1
            return (s, e)

        keyword_dict = {}
        for c in T:
            if c in keyword_dict:
                keyword_dict[c] += 1
            else:
                keyword_dict[c] = 1

        keyword_postions = []
        i = 0
        while i < len(S):
            if S[i] in keyword_dict:
                keyword_postions.append(i)
            i += 1

        keyword_dict_string = {}

        min_window = ""
        s, e = 0, len(keyword_postions)-1
        i = 0
        while i < len(keyword_postions):
            position = keyword_postions[i]
            keyword = S[position]
            if keyword in keyword_dict_string:
                keyword_dict_string[keyword] += 1
            else:
                keyword_dict_string[keyword] = 1
            if found_all(keyword_dict_string, keyword_dict):
                (s, e) = shrink_left(0, i, keyword_dict_string, keyword_dict, keyword_postions, S)
                min_window = S[keyword_postions[s]:keyword_postions[e]+1]
                break
            i += 1

        while True:
            looking_for = S[keyword_postions[s]]
            i = e + 1
            if i >= len(keyword_postions):
                return min_window
            while S[keyword_postions[i]] != looking_for:
                keyword_dict_string[S[keyword_postions[i]]] += 1
                i += 1
                if i >= len(keyword_postions):
                    return min_window
            else:
                keyword_dict_string[S[keyword_postions[i]]] += 1

            (s, e) = shrink_left(s, i, keyword_dict_string, keyword_dict, keyword_postions, S)
            if keyword_postions[e] - keyword_postions[s] + 1 < len(min_window):
                min_window = S[keyword_postions[s]:keyword_postions[e]+1]


def main():
    sol = Solution()
    S = "ADOBECODEBANC"
    S = "a"
    T = "ABC"
    T = "a"
    print sol.minWindow(S, T)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

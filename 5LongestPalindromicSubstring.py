# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/longest-palindromic-substring/

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

===Comments by Dabay===
从最长的字符串开始判断，直到长度为2。但是这样的算法会超时Time Limit Exceeded。
使用一个著名的算法，叫Manacher's ALGORITHM：
每一个字符之间加上一个#来隔开，遍历的时候，从每个字符往两边延生，记录最长子串的长度。
这里加入#，避免了回文字符串是奇数或偶数的问题。
最后，在生成的记录长度的数组中，找到最大回文子串即可。

S  #  a  #  b  #  b  #  a  #  b  #  c  #  b  #  a  #
P  1  2  1  2  5  2  1  4  1  2  1  6  1  2  1  2  1

mid记录包含最大右边界的回文子串的中心位置，max_right记录最大子串的右边界。

初始化位置0

对于每一个位置i
    如果i不超过max_right：
        判断基于mid对称点的回文长度是否超过边界
        如果没有超过边界：
            不用继续判断了，直接赋值为这个对称点的值，继续判断下一个i
        如果超过边界：
            在边界内的部分不用判断了（因为对称性，肯定是回文），继续寻找最长回文，记录长度
    如果i超过了max_right:
        寻找最长回文，记录长度

    如果max_right得到了拓展，更新mid和max_right
'''
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        s_list = ['#']
        for c in s:
            s_list.append(c)
            s_list.append('#')

        max_right = 0
        mid = 0
        p = [0 for _ in s_list]
        p[0] = 1

        for i in xrange(1, len(p)):
            if i <= max_right:
                if p[2*mid-i] < max_right-i:
                    p[i] = p[2*mid-i]
                    continue
                else:
                    j = max_right - i
                    while i + j < len(s_list) and i - j >= 0 and s_list[i+j] == s_list[i-j]:
                        j = j + 1
                    p[i] = j
            else:
                j = 1
                while i + j < len(s_list) and i - j >= 0 and s_list[i+j] == s_list[i-j]:
                    j = j + 1
                p[i] = j
            if max_right < p[i] + i - 1:
                max_right = p[i] + i - 1
                mid = i

        max_p = max(p)
        max_index = p.index(max_p)

        longest = ""
        for i in range(max_index-max_p+1, max_index+max_p):
            if s_list[i] == '#':
                continue
            longest = longest + s_list[i]
        return longest


def main():
    s = Solution()
    string = "cubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffmnzznmltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc"
    #string = "abbabcba"
    print s.longestPalindrome(string)

if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
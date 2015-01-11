# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

===Comments by Dabay===
维护一个变量max_so_far来记录到目前为止最大的不重复字符串长度，同时维护一个字符串，这个字符串必须包含正在检查的字符。
因为这个字符串可能继续增长，当长度超过max_so_far时，更新max_so_far。
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        max_so_far = 0
        longest = ""
        for char in s:
            if char in longest:
                longest = longest[(longest.index(char))+1:] + char
            else:
                longest = longest + char
                max_so_far = max(max_so_far, len(longest))
        return max_so_far


def main():
    s = Solution()
    string = "abcabcbb"
    print s.lengthOfLongestSubstring(string)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
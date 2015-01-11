# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        old_longest = []
        longest = []
        i = 0
        while i < len(s):
            #print i
            c = s[i]
            #print c
            if c not in longest:
                #print "c not in longest"
                #print "c is %s" % c
                longest.append(c)
                #print longest
            else:
                index = longest.index(c)
                #print index
                longest = longest[index+1:]
                longest.append(c)

            if len(longest) > len(old_longest):
                old_longest = list(longest)


            i = i + 1
        #print old_longest
        return len(old_longest)


def main():
    s = Solution()
    string = "abcabcbb"
    print s.lengthOfLongestSubstring(string)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
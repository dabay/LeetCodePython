# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        def is_palindrome(string):
            i = 0
            while i < len(string)/2:
                if string[i] != string[len(string)-1-i]:
                    return False
                i = i + 1
            return True

        def partition2(result, temp_list, rest_string):
            if len(rest_string) == 0:
                result.append(list(temp_list))
                return
            if len(rest_string) == 1:
                temp_list.append(rest_string)
                result.append(list(temp_list))
                return
            for i in xrange(1, len(rest_string)+1):
                prefix = rest_string[:i]
                if is_palindrome(prefix):
                    temp_list2 = list(temp_list)
                    temp_list2.append(prefix)
                    partition2(result, temp_list2, rest_string[i:])

        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]
        result = []
        partition2(result, [], s)
        return result

def main():
    s = Solution()
    print s.partition("kka")


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)
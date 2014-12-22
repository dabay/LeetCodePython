# -*- coding: utf8 -*-
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        def numDecodings2(s, index, index_num_dict):
            if index == 0:
                if s[0] == "0":
                    index_num_dict[0] = 0
                else:
                    index_num_dict[0] = 1
                return
            if index == 1:
                flag = 0
                if int(s[:2]) >= 10 and int(s[:2]) <= 26:
                    flag = 1
                if s[1] == "0":
                    index_num_dict[1] = flag
                else:
                    index_num_dict[1] = flag + 1
                return

            last_one = int(s[index])
            last_one_can_decoding = False
            if last_one != 0:
                last_one_can_decoding = True

            last_two = int(s[index-1:index+1])
            last_two_can_decoding = False
            if last_two >= 10 and last_two <= 26:
                last_two_can_decoding = True

            num = 0
            if last_one_can_decoding:
                num = num + index_num_dict[index-1]
            if last_two_can_decoding:
                num = num + index_num_dict[index-2]
            index_num_dict[index] = num

        index_num_dict = {}
        for i in xrange(len(s)):
            numDecodings2(s, i, index_num_dict)
            if index_num_dict[i] == 0:
                break

        if len(s)-1 not in index_num_dict.keys():
            return 0
        else:
            return index_num_dict[len(s)-1]


if __name__ == "__main__":
    s = Solution()
    print s.numDecodings("111")
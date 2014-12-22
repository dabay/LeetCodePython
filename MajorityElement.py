# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/majority-element/

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        if len(num) == 1:
            return num[0]
        dict_num = {}
        n = len(num)
        for i in xrange(n):
            if num[i] not in dict_num.keys():
                dict_num[num[i]] = 1
            else:
                dict_num[num[i]] = dict_num[num[i]] + 1
                if dict_num[num[i]] > n/2:
                    return num[i]



if __name__ == "__main__":
    s = Solution()
    list = [1,2,3,1,2,1,1,2,1,1,1]
    print s.majorityElement(list)

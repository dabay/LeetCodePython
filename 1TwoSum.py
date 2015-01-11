# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/two-sum/

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

===Comments by Dabay===
这道题描述中没有讲明对时间复杂度的要求。
用一个while循环嵌套另外一个while循环，时间复杂度为O(NlgN)。
这里可以用空间来换时间，用O(N)空间来存储每个数的位置，这样就可以用O(N)的时间来找到答案。
因为hash表的命中时间是O(1)。

但是，先遍历一次num，存储所有的数字到hash表中；再遍历一次来查找结果，还是会超时。

考虑其实不需要存储所有的数字到hash表中，因为只要在已经存在的hash表中有我们需要的答案就可以啦。
所以一次遍历的时候，查找是否有我们需要的答案，如果没有添加这个数字到hash表中。

此题答案要求的index是我们数组index+1的，所以返回的时候各加1。
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            expected = target - num[i]
            if expected in dict.keys():
                return (dict[expected]+1, i+1)
            dict[num[i]] = i


def main():
    s = Solution()
    nums = [-3,4,3,90]
    print s.twoSum(nums, 0)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
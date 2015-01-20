# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

15: 3Sum
https://oj.leetcode.com/problems/3sum/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

===Comments by Dabay===
先排序，然后从左到右固定一个数，在后边的数列中使用左右指针往中间靠拢的方法查找。

从左往右固定一个数(如果需要判断的数与之前的相等就跳过),
左右两个指针往中间靠拢的时候，能够保证不遗漏。(如果找到一组数据之后，左指针继续移动到下一个数不相等的数)
'''
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        num.sort()
        res = []
        for i in xrange(len(num)-2):
            if i>0 and num[i]==num[i-1]:
                continue
            target = 0 - num[i]
            j, k = i+1, len(num)-1
            while j < k:
                if num[j] + num[k] == target:
                    res.append([num[i], num[j], num[k]])
                    j = j + 1
                    while j<k and num[j]==num[j-1]:
                        j = j + 1
                elif num[j] + num[k] < target:
                    j = j + 1
                else:
                    k = k - 1
        return res

def main():
    sol = Solution()
    nums = [0,0,0,0,0]
    solutions = sol.threeSum(nums)
    for solution in solutions:
        print solution


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
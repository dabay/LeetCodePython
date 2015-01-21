# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

18: 4Sum
https://oj.leetcode.com/problems/4sum/

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

===Comments by Dabay===
k sum的问题就可以转化为k-1 sum，直到3 sum。
这道题可以使用空间来换时间，用一个hash表来记录两个数字的和，值存他们的坐标。
然后两次循环，判断是否在hash中是否有命中的值满足和为target。
如果有的话，因为两次循环是从小到大，应该要满足hash表的小坐标大于内循序的坐标。
'''
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        d = {}
        num.sort()
        for i in xrange(len(num)-1):
            for j in xrange(i+1, len(num)):
                sum2 = num[i]+num[j]
                if sum2 not in d:
                    d[sum2] = [[i,j]]
                else:
                    d[sum2].append([i,j])

        res = []
        for i in xrange(len(num)-3):
            for j in xrange(i+1, len(num)-2):
                x = target - (num[i] + num[j])
                if x in d:
                    for (m,n) in d[x]:
                        if m > j and [num[i],num[j],num[m],num[n]] not in res:
                            res.append([num[i],num[j],num[m],num[n]])
        return res


def main():
    sol = Solution()
    nums = [-2, -1, 0, 0, 1, 2]
    print sol.fourSum(nums, 0)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 1:
            return num[0]

        for i in xrange(1, len(num)):
            if num[i-1] <= num[i]:
                continue
            else:
                return num[i]
        else:
            return num[0]


def main():
    s = Solution()
    nums = [4, 5, 0, 1]
    print s.findMin(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    end = time.clock()
    print "%s sec" % (end - start)
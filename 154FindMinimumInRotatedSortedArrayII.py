# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

154: Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicates.

=== Comments by Dabay===
折半查找。因为有重复，每次继续查找之前，把右边的指针往左移动到和左指针的数不同。
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 1:
            return num[0]
        left_index, right_index = 0, len(num)-1
        return self.findMin2(num, left_index, right_index)

    def findMin2(self, num, i, j):
        while num[i] == num[j] and j > i:
            j -= 1
        if i == j:
            return num[i]
        if i + 1 == j:
            return min(num[i], num[j])
        if num[i] < num[j]:
            return num[i]
        k = (i + j) / 2
        if num[i] <= num[k]:
            return self.findMin2(num, k, j)
        else:
            return self.findMin2(num, i, k)


def main():
    sol = Solution()
    num = [10, 1, 10, 10, 10]
    print sol.findMin(num)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
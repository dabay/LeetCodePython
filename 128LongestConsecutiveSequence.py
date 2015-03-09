# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

128: Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.

=== Comments by Dabay===
需要O(n)的时间复杂度，肯定是使用哈希表。
遍历列表，如果是新的元素，往左右看，判读是否有元素已经在哈希表中了。
对于每一段连续的数字，用左右两端来记录这一段连续数字的长度。中间可以不用管了，因为每次往左右看的时候，肯定是先遇到这一段连续数字的两头。
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        hash_table = {}
        res = 0
        for n in num:
            if n in hash_table:
                continue
            hash_table[n] = 1
            count = 1
            left = right = 0
            if n - 1 in hash_table:
                left = hash_table[n-1]
            if n + 1 in hash_table:
                right = hash_table[n+1]
            count = count + left + right
            hash_table[n - left] = count
            hash_table[n + right] = count
            res = max(res, count)
        return res



def main():
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print sol.longestConsecutive(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
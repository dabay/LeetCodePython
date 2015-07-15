# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
208: Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

=== Comments by Dabay===
两个指针,滑动窗口。左指针不动，移动右指针。
找到之后，右指针+1，收缩左指针。
直到右指针指向结尾。

对于nlog(n)的解法，使用二分，处理扩界。
'''

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if len(nums)==0 or sum(nums) < s:
            return 0
        min_len = None
        left, right = 0, 0
        temp_sum = nums[0]
        while temp_sum < s:
            right += 1
            temp_sum += nums[right]
        min_len = right - left + 1
        while True:
            while temp_sum - nums[left] >= s:
                temp_sum -= nums[left]
                left += 1
            min_len = min(min_len, right-left+1)
            right += 1
            if right >= len(nums):
                return min_len
            else:
                temp_sum += nums[right]


def main():
    nums = [2,3,1,2,4,3]
    s = 7
    sol = Solution()
    print sol.minSubArrayLen(s, nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
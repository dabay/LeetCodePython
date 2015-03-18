# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

164: Maximum Gap
https://leetcode.com/problems/maximum-gap/

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.
Return 0 if the array contains less than 2 elements.
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

=== Comments by Dabay===
桶排序。
桶的个数为数组的长度。每个桶里面维护一个最大数和最小数。
利用这个最大数和最小数的差计算桶中的最大差，利用上一个桶的最大到下一个桶的最小计算桶之间的差。
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) <= 1:
            return 0
        if len(num) == 2:
            return abs(num[0]-num[1])
        minimum = min(num)
        maximum = max(num)
        bucket = [[None,None] for _ in num]
        range = ((maximum - minimum) / len(num)) + 1
        for n in num:
            bucket_index = (n - minimum) / range
            if bucket[bucket_index] == [None, None]:
                bucket[bucket_index] = [n, n]
            elif bucket[bucket_index][1] < n:
                bucket[bucket_index][1] = n
            elif bucket[bucket_index][0] > n:
                bucket[bucket_index][0] = n
        res = bucket[0][1] - bucket[0][0]
        pre_index = 0
        for i in xrange(1, len(bucket)):
            if bucket[i] == [None, None]:
                continue
            local_min, local_max = bucket[i]
            res = max(res, local_max-local_min, local_min-bucket[pre_index][1])
            pre_index = i
        return res


def main():
    sol = Solution()
    num = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588]
    print sol.maximumGap(num)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
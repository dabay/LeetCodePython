# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

===Comments by Dabay===
先计算中位数在合并后数组中的什么坐标为medium_pos。
同时考虑到，合并后数组的元素总数是奇数偶数的不同情况，用一个变量last来记录寻找到中位数的游标停下来的位置。
如果是奇数，这个last没有用；如果是偶数，用这个last和下一个可能的数求一个平均数。
'''

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        len_a, len_b = len(A), len(B)
        i = j = 0
        medium_pos = (len_a + len_b) / 2
        counter = 0
        last = None
        while counter < medium_pos:
            if i < len_a and j < len_b:
                if A[i] < B[j]:
                    last = A[i]
                    i = i + 1
                else:
                    last = B[j]
                    j = j + 1
            elif i < len_a:
                last = A[i]
                i = i + 1
            elif j < len_b:
                last = B[j]
                j = j + 1
            counter = counter + 1
        if (len_a + len_b) % 2 == 0:
            if i < len_a and j < len_b:
                return (last + min(A[i], B[j])) / 2.0
            elif i == len_a:
                return (last + B[j]) / 2.0
            elif j == len_b:
                return (last + A[i]) / 2.0
        else:
            if i < len_a and j < len_b:
                return min(A[i], B[j])
            elif i == len_a:
                return B[j]
            elif j == len_b:
                return A[i]


def main():
    s = Solution()
    A = [1, 2, 3, 4, 5]
    B = []
    print s.findMedianSortedArrays(A, B)

if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
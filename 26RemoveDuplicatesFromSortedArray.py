# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

26: Remove Duplicates from Sorted Array
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].

===Comments by Dabay===
一次循环，两个指针，一个指向最后插入的位置，另外一个一直往前面走。
    如果两个指针的数一样，二号指针继续走。
    如果不一样，把二号指针指向的数插入到一号指针的后面。
最后跟新数组，返回长度。
'''

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i,j = 0,0
        while j < len(A):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
            j += 1
        A = A[:i+1]
        return len(A)


def main():
    sol = Solution()
    print sol.removeDuplicates([1,1,2])


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

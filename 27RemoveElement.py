# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

27: Remove Element
https://oj.leetcode.com/problems/remove-element/

Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

===Comments by Dabay===
一次循环，两个指针，一个指向插入的位置，另外一个一直往前面走。
    如果二号指针的数就是需要删除的数，二号指针继续走。
    如果不是要删除的数，把二号指针指向的数移到一号指针的位置上，然后两个指针继续走。
最后跟新数组，返回长度。
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i = j = 0
        while j < len(A):
            if A[j] != elem:
                A[i] = A[j]
                i += 1
            j += 1
        A = A[:i]
        return len(A)


def main():
    sol = Solution()
    print sol.removeElement([1,1,2], 1)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

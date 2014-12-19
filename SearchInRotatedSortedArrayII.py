# -*- coding: utf8 -*-
'''
Follow up for "Search in Rotated Sorted Array":
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
这道题好奇怪，直接比较每个元素就可以accept，无语~
感觉能优化的，也就是array的后面一段，如果超过了rotate point，而且数字又比target大，就直接返回False
'''

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        for i in xrange(len(A)):
            if A[i] == target:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    l = [8,9,1,1,2,3,4,4,4,5]
    print s.search(l, 4)
# -*- coding: utf8 -*-
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3:
            return len(A)
        duplicated = 0
        x = A[0]
        i = 1
        while i < len(A):
            if A[i] == x:
                duplicated = duplicated + 1
                if duplicated < 2:
                    i = i + 1
                    continue
                else:
                    A.pop(i)
                    continue
            else:
                x = A[i]
                duplicated = 0
                i = i + 1
                continue
        return len(A)


if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([1,1,1,2,2,3])

# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
278: First Bad Version
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

=== Comments by Dabay===
Search from mid.  注意找mid的时候，如果两个数字很接近，这个mid算出来还是i，就直接返回。
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version > 50

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(0):
            return 0
        return self.badVersion(0, n)

    def badVersion(self, i, j):
        mid = (i + j) / 2
        if mid == i:
            return j
        if isBadVersion(mid):
            return self.badVersion(i, mid)
        else:
            return self.badVersion(mid, j)


def main():
    sol = Solution()
    print sol.firstBadVersion(100)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
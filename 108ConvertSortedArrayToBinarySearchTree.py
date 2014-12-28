# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        if len(num) == 1:
            return TreeNode(num[0])
        mid_index = len(num)/2
        root = TreeNode(num[mid_index])
        root.left = self.sortedArrayToBST(num[:mid_index])
        root.right = self.sortedArrayToBST(num[mid_index+1:])
        return root


if __name__ == "__main__":
    s = Solution()
    num = [i for i in xrange(1, 8)]
    root = s.sortedArrayToBST(num)
    print "Root's value: %s" % root.val

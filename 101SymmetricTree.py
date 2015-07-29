# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

101: Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3

===Comments by Dabay===
递归遍历树
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSameTree(root.left, root.right)

    def isMirrorTree(self, p, q):
        if p is None and q is None:
            return True
        if (p and q is None) or (p is None and q):
            return False
        if p.val == q.val:
            return self.isMirrorTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        else:
            return False

def main():
    sol = Solution()
    print sol.isSameTree(None)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

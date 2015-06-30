# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
226: Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

=== Comments by Dabay===
递归
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None or (root.left is None and root.right is None):
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


def main():
    root = TreeNode(4)
    l1 = TreeNode(2)
    l2 = TreeNode(7)
    root.left = l1
    root.right = l2
    m1 = TreeNode(1)
    m2 = TreeNode(3)
    m3 = TreeNode(6)
    m4 = TreeNode(9)
    l1.left = m1
    l1.right = m2
    l2.left = m3
    l2.right = m4
    sol = Solution()
    print sol.invertTree(root)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
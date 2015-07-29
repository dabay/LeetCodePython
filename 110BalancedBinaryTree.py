# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

110: Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

===Comments by Dabay===
递归. 这道题比较经典。
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
    def isBalanced(self, root):
        if root is None:
            return True
        if abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def max_depth(self, node):
        if node is None:
            return 0
        return max(self.max_depth(node.left), self.max_depth(node.right)) + 1


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right =TreeNode(4)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)
    root.right.left.right = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    root.left.left.left.right = TreeNode(5)
    sol = Solution()
    print sol.isBalanced(root)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

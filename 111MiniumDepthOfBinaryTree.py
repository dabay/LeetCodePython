# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

111: Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

===Comments by Dabay===
深度优先遍历。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root is None:
            return 0
        res = [99999999, 1]    # Min_Depth, Current_Depth
        self.DFS(root, res)
        return res[0]

    def DFS(self, node, res):
        if node.left is None and node.right is None:
            res[0] = min(res)
            return
        if node.left:
            res[1] += 1
            self.DFS(node.left, res)
            res[1] -= 1
        if node.right:
            res[1] += 1
            self.DFS(node.right, res)
            res[1] -= 1


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
    print sol.minDepth(root)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

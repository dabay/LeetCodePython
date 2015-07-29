# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

104: Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

===Comments by Dabay===
深度优先遍历
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
    def maxDepth(self, root):
        res = [0, 0]    #[max_depth, current_depth]
        self.DFS(root, res)
        return res[0]

    def DFS(self, node, res):
        if node:
            res[1] += 1
            res[0] = max(res)
            self.DFS(node.left, res)
            self.DFS(node.right, res)
            res[1] -= 1


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    sol = Solution()
    print sol.maxDepth(root)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

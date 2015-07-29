# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

112: Path Sum
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree
has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        res = [sum, 0, False]
        self.DFS(root, res)
        return res[2]

    def DFS(self, node, res):
        if res[2] == True:
            return
        if node.left is None and node.right is None:
            if res[0] == res[1] + node.val:
                res[2] = True
                return
        if node.left:
            res[1] += node.val
            self.DFS(node.left, res)
            res[1] -= node.val
        if node.right:
            res[1] += node.val
            self.DFS(node.right, res)
            res[1] -= node.val


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
    print sol.hasPathSum(root, 10)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

107: Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

===Comments by Dabay===
广度优先遍历
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        res = []
        if root is None:
            return []
        self.BFS([root], res)
        return res

    def BFS(self, node_list, res):
        if len(node_list) == 0:
            return
        new_node_list = []
        node_value_list = []
        for node in node_list:
            node_value_list.append(node.val)
            if node.left:
                new_node_list.append(node.left)
            if node.right:
                new_node_list.append(node.right)
        res.insert(0, node_value_list)
        self.BFS(new_node_list, res)


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    sol = Solution()
    print sol.levelOrderBottom(root)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

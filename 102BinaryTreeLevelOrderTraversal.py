# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

102: Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
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
    def levelOrder(self, root):
        res = []
        if root is None:
            return []
        self.levelOrder2([root], res)
        return res

    def levelOrder2(self, node_list, res):
        if len(node_list) == 0:
            return
        new_node_list = []
        node_list_values = []
        for node in node_list:
            node_list_values.append(node.val)
            if node.left:
                new_node_list.append(node.left)
            if node.right:
                new_node_list.append(node.right)
        res.append(node_list_values)
        self.levelOrder2(new_node_list, res)

def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    sol = Solution()
    print sol.levelOrder(root)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

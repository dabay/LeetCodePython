# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        def connect2(node_list):
            if len(node_list) == 0:
                return
            if node_list[0] is None:
                return

            for i in xrange(len(node_list)-1):
                node_list[i].next = node_list[i+1]

            if node_list[0].left is None:
                return
            children_list = []
            for node in node_list:
                children_list.append(node.left)
                children_list.append(node.right)
            connect2(children_list)

        connect2([root])

if __name__ == "__main__":
    s = Solution()
    root = TreeNode("root")
    root.left = TreeNode("left_child")
    root.right = TreeNode("right_child")
    s.connect(root)
    print root.left.next.val

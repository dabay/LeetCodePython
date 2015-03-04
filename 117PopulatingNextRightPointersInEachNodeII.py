# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

117: Populating Next Right Pointers in Each Node II
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?
Note:
You may only use constant extra space.
For example,
Given the following binary tree,
        1
       / \
      2   3
     / \   \
    4   5   7
After calling your function, the tree should look like:
        1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
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
        head = root
        while head:
            cur = head
            new_head = None
            pre = None
            while cur:
                if cur.left:
                    if new_head is None:
                        new_head = cur.left
                        pre = cur.left
                    else:
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if new_head is None:
                        new_head = cur.right
                        pre = cur.right
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next
            head = new_head


if __name__ == "__main__":
    s = Solution()
    root = TreeNode("root")
    root.left = TreeNode("left_child")
    root.right = TreeNode("right_child")
    s.connect(root)
    print root.left.next.val

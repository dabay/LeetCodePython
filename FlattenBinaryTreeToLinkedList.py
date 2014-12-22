# -*- coding: utf8 -*-
'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        def flatten2(node):
            if node is None:
                return None
            if node.left is None and node.right is None:
                return node
            tail_left_side = flatten2(node.left)
            tail_right_side = flatten2(node.right)
            head_left_side = node.left
            head_right_side = node.right

            node.left = None
            if head_left_side is not None:
                node.right = head_left_side
                if head_right_side is None:
                    return tail_left_side
                else:
                    tail_left_side.right = head_right_side
            else:
                node.right = head_right_side
            return tail_right_side

        if root is None:
            return

        tail_left_side = flatten2(root.left)
        tail_right_side = flatten2(root.right)
        head_left_side = root.left
        head_right_side = root.right

        root.left = None
        if head_left_side is not None:
            root.right = head_left_side
            tail_left_side.right = head_right_side
        else:
            root.right = head_right_side

if __name__ == "__main__":
    tn1 = TreeNode(1)
    tn2 = TreeNode(2)
    tn3 = TreeNode(3)
    tn1.left = tn2
    tn2.left = tn3

    s = Solution()
    s.flatten(tn1)

    n = tn1
    while n:
        print str(n.val) + "->",
        n = n.right
    print "None"


# -*- coding: utf8 -*-
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def isValidBST2(root, m):
            # if root.left is None and root.right is None:
            #     return (True, root.val)

            value = root.val
            if root.left is not None:
                (left_valide, left_max) = isValidBST2(root.left, "max")
                if left_valide is False or value <= left_max:
                    return (False, 0)
            if root.right is not None:
                (right_valide, right_min) = isValidBST2(root.right, "min")
                if right_valide is False or value >= right_min:
                    return (False, 0)

            node = root
            if m == "max":
                while node.right is not None:
                    node = node.right
                return (True, node.val)
            elif m == "min":
                while node.left is not None:
                    node = node.left
                return (True, node.val)
            else:
                return (True, 0)

        if root is None:
            return True
        return isValidBST2(root, "")[0]

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(-29)
    r = TreeNode(37)
    r.left = TreeNode(49)
    r.right = TreeNode(93)
    root.right = r
    print s.isValidBST(root)

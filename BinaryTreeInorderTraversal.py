# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        # def inorderTraversal2(result, node):
        #     if node is None:
        #         return
        #     inorderTraversal2(result, node.left)
        #     result.append(node.val)
        #     inorderTraversal2(result, node.right)
        #
        # result = []
        # inorderTraversal2(result, root)
        # return result

        stack = []
        node = root
        result = []
        visited = []
        while node is not None:
            if node.left not in visited:
                while node.left is not None:
                    stack.append(node)
                    node = node.left
            result.append(node.val)
            visited.append(node)
            if node.right is not None:
                node = node.right
                continue
            else:
                if len(stack) > 0:
                    node = stack.pop()
                    continue
                else:
                    break
        return result


if __name__ == "__main__":
    root = TreeNode(3)
    tn2 = TreeNode(1)
    tn3 = TreeNode(2)
    root.left = tn2
    tn2.right = tn3

    s = Solution()
    print s.inorderTraversal(root)
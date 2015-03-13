# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

145: Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given a binary tree, return the postorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
Note: Recursive solution is trivial, could you do it iteratively?

=== Comments by Dabay===

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
    def postorderTraversal(self, root):
        if root is None:
            return []

        stack = [root]
        res = []
        while len(stack) > 0:
            node = stack.pop(0)
            res.insert(0, node.val)
            if node.left:
                stack.insert(0, node.left)
            if node.right:
                stack.insert(0, node.right)
        return res


def main():
    s = Solution()
    tn1 = TreeNode(1)
    tn2 = TreeNode(2)
    tn3 = TreeNode(3)
    tn1.right = tn2
    tn2.left = tn3
    print s.postorderTraversal(tn1)


if __name__ == "__main__":
    import time
    start_time = time.clock()
    main()
    print "%s sec" % (time.clock() - start_time)
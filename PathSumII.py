# -*- coding: utf8 -*-
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

#Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def search_tree(result, pathlist, treenode, number):
            if treenode is None:
                return

            if treenode.left is None and treenode.right is None:
                if treenode.val == number:
                    pathlist.append(treenode.val)
                    result.append(list(pathlist))
                    pathlist.pop(-1)
            else:
                pathlist.append(treenode.val)
                if treenode.left is not None:
                    search_tree(result, pathlist, treenode.left, number-treenode.val)
                if treenode.right is not None:
                    search_tree(result, pathlist, treenode.right, number-treenode.val)
                pathlist.pop(-1)

        result = []
        search_tree(result, [], root, sum)
        return result

if __name__ == "__main__":
    tn41 = TreeNode(7)
    tn42 = TreeNode(2)
    tn43 = TreeNode(5)
    tn44 = TreeNode(1)
    tn31 = TreeNode(11)
    tn31.left = tn41
    tn31.right = tn42
    tn32 = TreeNode(13)
    tn33 = TreeNode(4)
    tn33.left = tn43
    tn33.right = tn44
    tn21 = TreeNode(4)
    tn21.left = tn31
    tn22 = TreeNode(8)
    tn22.left = tn32
    tn22.right = tn33
    tn1 = TreeNode(5)
    tn1.left = tn21
    tn1.right = tn22

    s = Solution()
    print s.pathSum(tn1, 22)

# -*- coding: utf8 -*-
'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):

        def generateTrees2(min_val, max_val):
            if min_val > max_val:
                return [None]
            if min_val == max_val:
                tn = TreeNode(min_val)
                return [tn]
            head_nodes = []
            for root_val in xrange(min_val, max_val+1):
                left_nodes = generateTrees2(min_val, root_val-1)
                right_nodes = generateTrees2(root_val+1,max_val)
                for ln in left_nodes:
                    for rn in right_nodes:
                        root_node = TreeNode(root_val)
                        root_node.left = ln
                        root_node.right = rn
                        head_nodes.append(root_node)
            return head_nodes

        return generateTrees2(1, n)

if __name__ == "__main__":
    s = Solution()
    tnl = s.generateTrees(10)
    for tn in tnl:
        print tn.val
    print len(tnl)
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

124: Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
For example:
Given the below binary tree,
       1
      / \
     2   3
Return 6.

=== Comments by Dabay===
每个节点可能是负数。对于每个节点来说，因为不知道其父节点，所以包含它的最大路径就是以下4个中的一个：
    - 节点本身
    - 节点本身 + 包含其左子节点的最大路径
    - 节点本身 + 包含其右子节点的最大路径
    - 节点本身 + 包含其左子节点的最大路径 + 包含其右子节点的最大路径

因为要连接成一个路径，所以递归函数返回的值不能同时包含左右节点。
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer

    def maxPathSum(self, root):
        if root is None:
            Solution.max_path_sum = 0
        else:
            Solution.max_path_sum = root.val
        self.maxPathSum2(root)
        return Solution.max_path_sum

    def maxPathSum2(self, node):
        if node is None:
            return 0
        max_sum_left = max(0, self.maxPathSum2(node.left))
        max_sum_right = max(0, self.maxPathSum2(node.right))
        max_sum = max(node.val, node.val+max_sum_left, node.val+max_sum_right)
        Solution.max_path_sum = max(Solution.max_path_sum, node.val+max_sum_left+max_sum_right)
        return max_sum


def main():
    sol = Solution()
    root = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    root.left = node1
    root.right = node2
    node3 = TreeNode(13)
    node4 = TreeNode(4)
    node2.left = node3
    node2.right = node4
    node4.right = TreeNode(1)
    node5 = TreeNode(11)
    node1.left = node5
    node5.left = TreeNode(7)
    node5.right = TreeNode(2)
    print sol.maxPathSum(root)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
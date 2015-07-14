# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
235: Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

=== Comments by Dabay===
找最接近根部的共同祖先节点。测试数据p q可能不是按照大小顺序的，所以判断一下。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if (p and p.val == root.val) or (q and q.val == root.val):
            return root
        if p and q and p.val > q.val:
            p, q = q, p
        if q and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


def main():
    root = TreeNode(6)
    l11 = TreeNode(2)
    l12 = TreeNode(8)
    root.left = l11
    root.right = l12
    l21 = TreeNode(0)
    l22 = TreeNode(4)
    l23 = TreeNode(7)
    l24 = TreeNode(9)
    l11.left = l21
    l11.right = l22
    l12.left = l23
    l12.right = l24
    l31 = TreeNode(3)
    l32 = TreeNode(5)
    l22.left = l31
    l22.right = l32
    sol = Solution()
    print sol.lowestCommonAncestor(root, l11, l12).val
    print sol.lowestCommonAncestor(root, l11, l22) == l11


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
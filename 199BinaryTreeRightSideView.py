# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
199: Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4].

=== Comments by Dabay===
把同一级的节点按顺序记录下来，依次pop出来，并记录下一级的节点，把最右边放结果集中。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root is None:
            return []
        res = []
        nodes = [root]
        res.append(root.val)
        self.go_next_level(nodes, res)
        return res


    def go_next_level(self, nodes, res):
        next_nodes = []
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node.left is not None:
                next_nodes.append(node.left)
            if node.right is not None:
                next_nodes.append(node.right)
        else:
            if len(next_nodes) > 0:
                res.append(next_nodes[-1].val)
                nodes = next_nodes
                self.go_next_level(nodes, res)


def main():
    root = TreeNode(1)
    l1 = TreeNode(2)
    l2 = TreeNode(3)
    root.left = l1
    root.right = l2
    m1 = TreeNode(5)
    m2 = TreeNode(4)
    l1.right = m1
    l2.right = m2
    sol = Solution()
    print sol.rightSideView(root)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
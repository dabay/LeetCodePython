# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
257: Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:
   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:
["1->2->5", "1->3"]

=== Comments by Dabay===
DFS.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        paths = []
        if root is not None:
            self.binaryTreePaths2(root, paths, [])
            for path in paths:
                path_str = "->".join([str(v) for v in path])
                res.append(path_str)
        return res

    def binaryTreePaths2(self, root, paths, path):
        if root.left is None and root.right is None:
            path.append(root.val)
            paths.append(list(path))
            path.pop()
            return
        if root.left is not None:
            path.append(root.val)
            self.binaryTreePaths2(root.left, paths, path)
            path.pop()
        if root.right is not None:
            path.append(root.val)
            self.binaryTreePaths2(root.right, paths, path)
            path.pop()


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    sol = Solution()
    print sol.binaryTreePaths(root)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
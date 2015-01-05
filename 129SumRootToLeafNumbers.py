# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
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
    def sumNumbers(self, root):
        def DFS(root, paths, temp_path):
            if root is None:
                return
            if root.left is None and root.right is None:
                paths.append(temp_path + str(root.val))
                return
            DFS(root.left, paths, temp_path + str(root.val))
            DFS(root.right, paths, temp_path + str(root.val))


        if root is None:
            return 0
        paths = []
        DFS(root, paths, "")
        result = 0
        for path in paths:
            result = result + int(path)
        return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    print s.sumNumbers(root)


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)
# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

99: Recover Binary Search Tree
https://oj.leetcode.com/problems/recover-binary-search-tree/

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

===Comments by Dabay===
这道题很厉害，确实是难题。
首先需要搞明白如何做O(1)空间的BST遍历：
    因为先遍历左子树，所以把父节点及其右子树挂到左子树的最右边是不影响顺序的。
    注意，当遍历到原左子树最右边的时候，实际上又回到了父节点。这时就需要还原树结构，即重新让原左子树最右边指向Null。
    这时，指针又回到父节点，判断父节点之后，指针指向其右子树，继续。。。

还有一个需要的注意的判断两个错误节点，当错误节点出现的时候，这个值肯定之前遍历的值小。
    1 2 3 9 6 7 8 5 10  此时，9和5应该交换
    1 2 3 9 5 10 12 13  此时，9和5应该交换
所以，当第一组数据到6的时候，发现比9小，9肯定是一个错误数据，但是6不一定是。
当第二组数据到5的时候，发现比9小，9一定是错误数据，而且5开始都是升序，5也是应该交换的。
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        mistake_nodes = []
        previous = None
        cur = root
        while cur:
            if cur.left is None:

                if previous and previous.val > cur.val:
                    if len(mistake_nodes) == 0:
                        mistake_nodes.append(previous)
                        mistake_nodes.append(cur)
                    else:
                        mistake_nodes[-1] = cur
                previous = cur

                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right

                if tmp.right is None:
                    tmp.right = cur
                    cur = cur.left
                else:
                    tmp.right = None

                    if previous and previous.val > cur.val:
                        if len(mistake_nodes) == 0:
                            mistake_nodes.append(previous)
                            mistake_nodes.append(cur)
                        else:
                            mistake_nodes[-1] = cur
                    previous = cur

                    cur = cur.right
        mistake_nodes[0].val, mistake_nodes[1].val = mistake_nodes[1].val, mistake_nodes[0].val
        return root


def main():
    sol = Solution()
    root = TreeNode(0)
    node2 = TreeNode(1)
    root.left = node2
    # node3 = TreeNode(3)
    # node2.left = node3
    sol.recoverTree(root)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)


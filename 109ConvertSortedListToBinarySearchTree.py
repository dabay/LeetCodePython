# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        def sortedArrayToBST(array):
            if len(array) == 0:
                return None
            if len(array) == 1:
                return TreeNode(array[0])
            mid_index = len(array)/2
            root = TreeNode(array[mid_index])
            root.left = sortedArrayToBST(array[:mid_index])
            root.right = sortedArrayToBST(array[mid_index+1:])
            return root

        sorted_list = []
        ln = head
        while ln is not None:
            sorted_list.append(ln.val)
            ln = ln.next

        return sortedArrayToBST(sorted_list)


if __name__ == "__main__":
    s = Solution()
    i = 1
    head = ListNode(i)
    ln = head
    i = i + 1
    while i < 8:
        ln2 = ListNode(i)
        ln.next = ln2
        ln = ln2
        i = i + 1
    root = s.sortedListToBST(head)
    print "root's value: %s" % root.val
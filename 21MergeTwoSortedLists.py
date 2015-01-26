# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

21: Merge Two Sorted Lists
https://oj.leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

===Comments by Dabay===
基本链表的操作。先做一个头节点，用两个指针来记录两个链表的位置。
比较两个链表的节点，把小的挂后边，之后移动指针。
最后，当一个链表已经比较完了之后，把另外一个链表中剩下的部分挂上。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        node = root = ListNode(0)
        node1 = l1
        node2 = l2
        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        if node1:
            node.next = node1
        else:
            node.next = node2
        return root.next


def main():
    sol = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    merged = sol.mergeTwoLists(l1, l2)
    node = merged
    while node:
        print "%s ->" % node.val,
    print "End"


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
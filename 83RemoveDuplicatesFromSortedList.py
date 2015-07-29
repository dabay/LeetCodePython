# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

83: Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

===Comments by Dabay===
两个指针
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while True:
            while fast and slow.val == fast.val:
                fast = fast.next
            slow.next = fast
            if fast is None:
                break
            else:
                slow, fast = fast, fast.next
        return head


def main():
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print sol.deleteDuplicates(head)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

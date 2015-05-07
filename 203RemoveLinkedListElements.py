# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

203: Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.
Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

=== Comments by Dabay===
基本链表操作。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        pre_head = ListNode(0)
        pre_head.next = head
        cur = pre_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return pre_head.next


def print_list_node(head):
    cur = head
    while cur:
        print "{}->".format(cur.val),
        cur = cur.next
    print "NULL"


def main():
    cur = head = ListNode(1)
    for val in (2, 6, 3, 4, 5, 6):
        cur.next = ListNode(val)
        cur = cur.next
    sol = Solution()
    print_list_node(sol.removeElements(head, 6))


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
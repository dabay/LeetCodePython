# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
206: Reverse Linked List
https://leetcode.com/problems/word-ladder-ii/

Reverse a singly linked list.

=== Comments by Dabay===
用三个变量来记录节点：pre,left,right
每次让left指向pre，然后三个变量往后面移动。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        pre = head
        left = head.next
        head.next = None
        right = left.next
        while right:
            left.next = pre
            pre = left
            left = right
            right = left.next
        left.next = pre
        return left


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
    print_list_node(head)
    sol = Solution()
    print_list_node(sol.reverseList(head))


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
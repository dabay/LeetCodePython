# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/insertion-sort-list/

Sort a linked list using insertion sort.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        def insert(head, node, end):
            if node.val < head.val:
                node.next = head
                return (node, end)
            n = head
            while n.next.val < node.val and n != end:
                n = n.next

            if n == end:
                node.next = end.next
                n.next = node
                return (head, node)
            else:
                end.next = node.next
                node.next = n.next
                n.next = node
                return (head, end)

        if head is None or head.next is None:
            return head
        if head.next.next is None:
            if head.val <= head.next.val:
                return head
            else:
                new_head = head.next
                new_head.next = head
                head.next = None
                return new_head

        new_head = head
        new_end = head
        cursor = head.next
        new_end.next = cursor.next
        while cursor:
            (new_head, new_end) = insert(new_head, cursor, new_end)
            cursor = new_end.next

        return new_head


def main():
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(1)
    # n3 = ListNode(3)
    # n4 = ListNode(2)
    n1.next = n2
    # n2.next = n3
    # n3.next = n4

    n = n1
    while n:
        print n.val, "->",
        n = n.next
    print

    s.insertionSortList(n1)

    n = n1
    while n:
        print n.val, "->",
        n = n.next
    print


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)

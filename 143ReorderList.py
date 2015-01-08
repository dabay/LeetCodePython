# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/reorder-list/

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

比较烦做这类题，思路比较简单，实现的时候却很麻烦。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return
        slow = fast = head
        while fast.next:
            fast = fast.next.next
            if fast is None:
                break
            slow = slow.next

        node1 = slow.next
        node2 = slow.next.next
        slow.next.next = None
        slow.next = None

        while node2:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3

        n1 = head
        n2 = node1
        while n2:
            n3 = n1.next
            n4 = n2.next
            n1.next = n2
            n2.next = n3
            n1 = n3
            n2 = n4


def main():
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    n = n1
    while n:
        print n.val, "->",
        n = n.next
    print

    s.reorderList(n1)

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
# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        def merge(head1, head2):
            new_head = end = ListNode(0)
            n1 = head1
            n2 = head2
            while n1 and n2:
                if n1.val < n2.val:
                    end.next = n1
                    end = n1
                    n1 = n1.next
                else:
                    end.next = n2
                    end = n2
                    n2 = n2.next
            if n1 is not None:
                end.next = n1
            if n2 is not None:
                end.next = n2
            return new_head.next

        if head is None or head.next is None:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow_next = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(slow_next)

        return merge(left, right)


def main():
    s = Solution()
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(1)
    n4 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    n = n1
    while n:
        print n.val, "->",
        n = n.next
    print

    head = s.sortList(n1)

    n = head
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

# -*- coding: utf8 -*-
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        new_head = ListNode(-1)
        new_head.next = head
        pointer = new_head
        less_end = new_head

        while pointer.next is not None:
            if pointer.next.val < x:
                if less_end == pointer:
                    pointer = pointer.next
                    less_end = pointer
                else:
                    to_insert = pointer.next
                    pointer.next = pointer.next.next
                    to_insert.next = less_end.next
                    less_end.next = to_insert
                    less_end = to_insert
            else:
                pointer = pointer.next
        return new_head.next


if __name__ == "__main__":
    s = Solution()
    ln1 = ListNode(1)
    ln2 = ListNode(4)
    ln3 = ListNode(3)
    ln4 = ListNode(2)
    ln5 = ListNode(5)
    ln6 = ListNode(2)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5
    ln5.next = ln6
    ln = ln1
    while ln is not None:
        print "%s ->" % ln.val,
        ln = ln.next
    print "None"

    ln = s.partition(ln1, 3)

    while ln is not None:
        print "%s ->" % ln.val,
        ln = ln.next
    print "None"

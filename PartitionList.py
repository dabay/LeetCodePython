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
        if hea
        pointer = head
        less_start = None
        less_end = None
        greater_start = None
        greater_end = None
        while pointer is not None:
            print pointer.val
            if pointer.val >= x:
                next_pointer = pointer.next
                #add_to_greater(pointer)
                if greater_start is None:
                    greater_start = pointer
                    greater_end = pointer
                    #greater_end.next = None
                else:
                    greater_end.next = pointer
                    greater_end = pointer
                    #greater_end.next = None

                pointer = next_pointer
            else:
                next_pointer = pointer.next
                #add_to_less(pointer)
                if less_start is None:
                    less_start = pointer
                    less_end = pointer
                else:
                    less_end.next = pointer
                    less_end = pointer
                pointer = next_pointer
        greater_end.next = None
        less_end.next = greater_start
        return less_start


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

# -*- coding: utf8 -*-
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return None
        cursor = head
        step_from_head_to_tail = 0
        while cursor.next is not None:
            cursor = cursor.next
            step_from_head_to_tail = step_from_head_to_tail + 1

        node_count = step_from_head_to_tail + 1
        k = k % node_count

        if step_from_head_to_tail + 1 < k:
            return head

        step_from_head_to_new_head = step_from_head_to_tail - (k - 1)
        step_from_head_to_new_tail = step_from_head_to_new_head - 1

        cursor.next = head
        step = 0
        while step <= step_from_head_to_new_tail:
            #print "here"
            cursor = cursor.next
            step = step + 1

        new_head = cursor.next
        cursor.next = None

        return new_head


if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(4)
    ln5 = ListNode(5)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5
    head = ln1
    while head is not None:
        print "%s->" % head.val,
        head = head.next
    print "NULL"


    s = Solution()
    head = s.rotateRight(ln1, 2)

    while head is not None:
        print "%s->" % head.val,
        head = head.next
    print "NULL"



  

# -*- coding: utf8 -*-
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        if head.next is None:
            return head

        new_head = ListNode(-1)
        new_tail = new_head
        pointer = head
        #value = pointer.val
        dup = False
        while pointer.next is not None:
            if pointer.val == pointer.next.val:
                dup = True
                pointer = pointer.next
                continue
            else:
                if dup is True:
                    dup = False
                    pointer = pointer.next
                    continue
                else:
                    new_tail.next = pointer
                    new_tail = pointer
                    #new_tail.next = None
                    pointer = pointer.next
                    continue
        if dup is False:
            new_tail.next = pointer
        else:
            new_tail.next = None
        return new_head.next



if __name__ == "__main__":
    s = Solution()
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(3)
    ln5 = ListNode(4)
    ln6 = ListNode(4)
    ln7 = ListNode(5)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5
    ln5.next = ln6
    ln6.next = ln7
    ln = ln1
    while ln is not None:
        print "%s ->" % ln.val,
        ln = ln.next
    print "None"

    ln = s.deleteDuplicates(ln1)

    while ln is not None:
        print "%s ->" % ln.val,
        ln = ln.next
    print "None"

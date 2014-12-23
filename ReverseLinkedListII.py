# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None or m == n:
            return head
        safeG = ListNode(-1)
        safeG.next = head
        pointer = safeG
        index = 1
        pre_reverse_node = None
        post_reverse_node = None
        reverse_list = []
        while pointer is not None:
            if index == m:
                pre_reverse_node = pointer
                index = index + 1
                pointer = pointer.next
                continue
            if index == n+1:
                reverse_list.append(pointer)
                post_reverse_node = pointer.next
                break
            if index > m and index <= n:
                reverse_list.append(pointer)
                index = index + 1
                pointer = pointer.next
                continue
            index = index + 1
            pointer = pointer.next

        for i in xrange(len(reverse_list)-1, -1, -1):
            pre_reverse_node.next = reverse_list[i]
            pre_reverse_node = pre_reverse_node.next
        pre_reverse_node.next = post_reverse_node

        return safeG.next


def print_linked_list(listnode):
    while listnode is not None:
        print "%s->" % listnode.val,
        listnode = listnode.next
    print "NONE"


if __name__ == "__main__":
    s = Solution()
    ln3 = ListNode(3)
    ln5 = ListNode(5)
    ln3.next = ln5
    print_linked_list(ln3)
    new_head = s.reverseBetween(ln3, 1, 2)
    print_linked_list(new_head)
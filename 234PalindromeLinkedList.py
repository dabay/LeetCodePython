# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
234: Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.
Could you do it in O(n) time and O(1) space?

=== Comments by Dabay===
在中间截断，把后边半截reverse，然后比较两个链，(可选)最后在把reverse的链恢复放在后面。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        head2 = self.cut_middle(head)
        head2 = self.reverse(head2)
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        else:
            return True

    def cut_middle(self, head):
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        i = (l-1) / 2
        c = 0
        node = head
        while c < i:
            c += 1
            node = node.next
        res = node.next
        node.next = None
        return res

    def get_len(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        a = head
        b = a.next
        a.next = None
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        return a


def main():
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(2)
    ln5 = ListNode(1)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5
    sol = Solution()
    print sol.isPalindrome(ln1)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
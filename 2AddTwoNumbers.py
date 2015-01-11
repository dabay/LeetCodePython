# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/add-two-numbers/

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        ret = l1
        c1 = l1
        c2 = l2
        carry = 0

        v = c1.val + c2.val + carry

        if v >= 10:
            v = v - 10
            carry = 1
        else:
            carry = 0
        c1.val = v

        while c1.next is not None and c2.next is not None:
            c1 = c1.next
            c2 = c2.next
            v = c1.val + c2.val + carry
            carry = 0
            if v >= 10:
                v = v - 10
                carry = 1
            else:
                carry = 0
            c1.val = v

        if c1.next is None and c2.next is None:
            if carry == 1:
                c1.next = ListNode(1)
                return ret
            return ret

        if c1.next is None and c2.next is not None:
            tail = c2.next
            while c2.next is not None:
                c2 = c2.next
                v = c2.val + carry

                if v >= 10:
                    v = v -10
                    carry = 1
                else:
                    carry = 0
                c2.val = v
            if carry == 1:
                c2.next = ListNode(1)
            c1.next = tail
            return ret

        if c1.next is not None and c2.next is None:
            while c1.next is not None:
                c1 = c1.next
                v = c1.val + carry
                if v >= 10:
                    v = v -10
                    carry = 1
                else:
                    carry = 0
                c1.val = v
            if carry == 1:
                c1.next = ListNode(1)
            return ret

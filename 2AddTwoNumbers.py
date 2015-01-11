# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/add-two-numbers/

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

===Comments by Dabay===
这道题没有要求不使用额外的空间。思路比较简单，就是逐个加起来的同时考虑进位。
那就在已有的空间上操作，主要是处理一些细节问题，如末尾有进位、两个数组不一样长等等。
我这里为了省事，当l1不够l2长的时候，用了额外的空间。
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

        node1, node2, carry, end = l1, l2, 0, None
        while node1 or node2:
            if not node1:
                node1 = ListNode(0)
                end.next = node1
            if not node2:
                node2 = ListNode(0)
            v = node1.val + node2.val + carry
            carry = 0
            if v >= 10:
                v = v - 10
                carry = 1
            node1.val = v
            end = node1
            node1 = node1.next
            node2 = node2.next
        if carry:
            end.next = ListNode(1)
        return l1


def main():
    root1 = ListNode(2)
    root1.next = ListNode(4)
    root1.next.next = ListNode(3)
    root2 = ListNode(5)
    root2.next = ListNode(6)
    root2.next.next = ListNode(4)
    s = Solution()
    root = s.addTwoNumbers(root1, root2)
    node = root
    while node:
        print "%s->" % node.val,
        node = node.next
    print "None"


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
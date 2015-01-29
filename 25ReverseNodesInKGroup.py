# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

===Comments by Dabay===
前面加一个辅助head。
每次处理k个元素，如果最后剩下的元素不足k，直接加到末尾。

reverse处理k个元素的时候，需要两个指针：指向第一个元素的前一个指针，以及 最后一个元素的后一个指针。
记得返回新的reverse之后的最后一个指针作为，下一次reverse的第一个参数。

reverse的时候用三个指针分别代表原链表中的pre,cur,next。

因为每次都先找到需要k个元素的区间，然后在调整指针，相当于遍历两次了，应该再改进一些...
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        def reverse(previous, after):
            new_previous = previous.next
            pre = previous.next
            cur = pre.next
            while cur != after:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            previous.next = pre
            new_previous.next = after
            return new_previous

        previous = new_head = ListNode(0)
        new_head.next = n = head
        counter = 0
        while n:
            n = n.next
            counter = counter + 1
            if counter == k:
                previous = reverse(previous, n)
                counter = 0
        return new_head.next


def print_listnode(node):
    while node:
        print "%s->" % node.val,
        node = node.next
    print "END"


def main():
    sol = Solution()
    node = root = ListNode(1)
    for i in xrange(2, 15):
        node.next = ListNode(i)
        node = node.next
    print_listnode(root)
    print_listnode(sol.reverseKGroup(root, 1))


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

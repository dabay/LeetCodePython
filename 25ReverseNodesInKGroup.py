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

reverse处理k个元素的时候，需要两个指向第一个元素的前一个指针，以及 最后一个元素的后一个指针。
记得返回新的reverse之后的最后一个指针作为，下一次reverse的第一个参数。
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
            ret = pre = previous.next
            cur = pre.next
            pre.next = after
            while cur != after:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            previous.next = pre
            return ret


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


def main():
    s = Solution()
    ln = ListNode(1)
    ln.next = ListNode(2)
    ln.next.next = ListNode(3)
    ln.next.next.next = ListNode(4)
    ln.next.next.next.next = ListNode(5)
    node = s.reverseKGroup(ln, 2)
    while node:
        print "%s->" % node.val,
        node = node.next
    print "None"


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

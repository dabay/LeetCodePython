# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

24: Swap Nodes in Pairs
https://oj.leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

===Comments by Dabay===
链表的操作。主要就是赋值next的时候，如果这个next本来指向的node还有用，就把它先记录下来。
这里用previous指向要交换的一对node的前面一个node。要交换的node依次为node1和node2。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        previous = new_head = ListNode(0)
        new_head.next = head
        while previous and previous.next and previous.next.next:
            node1 = previous.next
            node2 = node1.next
            node1.next = node2.next
            previous.next = node2
            node2.next = node1
            previous = node1
        return new_head.next


def print_listnode(node):
    while node:
        print "%s->" % node.val,
        node = node.next
    print "END"


def main():
    sol = Solution()
    node = root = ListNode(1)
    for i in xrange(2, 5):
        node.next = ListNode(i)
        node = node.next
    print_listnode(root)
    print_listnode(sol.swapPairs(root))


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

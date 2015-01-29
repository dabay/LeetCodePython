# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

25: Reverse Nodes in k-Group
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
用一个栈来记录k个元素，当栈不满的时候入栈，当栈大小到k的时候处理这k个元素。
最后检查栈是否为空
    如果为空，末尾加None
    如果不为空，末尾指向栈底的元素即可（因为入栈的时候，并没有破坏链表顺序）
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
        previous = new_head = ListNode(0)
        node = new_head.next = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
            if len(stack) == k:
                while len(stack) > 0:
                    pop_node = stack.pop()
                    previous.next = pop_node
                    previous = pop_node
        else:
            if len(stack) > 0:
                previous.next = stack[0]
            else:
                previous.next = None
        return new_head.next


def print_listnode(node):
    while node:
        print "%s->" % node.val,
        node = node.next
    print "END"


def main():
    sol = Solution()
    node = root = ListNode(1)
    for i in xrange(2, 3):
        node.next = ListNode(i)
        node = node.next
    print_listnode(root)
    print_listnode(sol.reverseKGroup(root, 2))


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)

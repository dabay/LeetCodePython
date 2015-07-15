# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
237: Delete Node in a Linked List
https://leetcode.com/problems/power-of-two/

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.

=== Comments by Dabay===
只有对这个node的信息。
如果直接node=node.next是不行的，python的参数是传值。如果要传址，可以用类似[node]的方式传递一个list。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def main():
    node = ListNode(1)
    node.next = ListNode(2)
    to_del = ListNode(3)
    node.next.next = to_del
    node.next.next.next = ListNode(4)
    sol = Solution()
    sol.deleteNode(to_del)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
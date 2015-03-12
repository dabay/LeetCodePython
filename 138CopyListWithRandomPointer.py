# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

138: Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.

=== Comments by Dabay===
请参考：http://blog.csdn.net/linhuanmars/article/details/22463599
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None

        pool = {}
        new_head = RandomListNode(head.label)
        pool[head] = new_head
        pre_new = new_head
        cur = head.next
        while cur:
            new_node = RandomListNode(cur.label)
            pool[cur] = new_node
            pre_new.next = new_node
            pre_new = new_node
            cur = cur.next

        cur = head
        while cur:
            if cur.random is not None:
                pool[cur].random = pool[cur.random]
            cur = cur.next

        return new_head


def main():
    sol = Solution()
    head = RandomListNode(0)
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    head.next = node1
    node1.next = node2
    head.random = node1
    new_head = sol.copyRandomList(head)
    print new_head.label


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
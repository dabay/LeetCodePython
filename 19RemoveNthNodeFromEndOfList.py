# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

19: Remove Nth Node From End of List
https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

===Comments by Dabay===
那种两个指针同时走的解法，应该是不符合题意的。人家要求的一次pass，你两个指针同时走，实际上是2次pass了。
思路一：
    遍历的时候，把每个node放到一个栈中，然后更加n弹出到相应的位置删除节点。空间复杂度为ListNode的长度。
思路二：
    用一个大小为n+1的队列来记录指针之前的n个节点。当指针到最后的时候，删除队列中的第二元素。空间复杂度为n+1。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        cursor = new_head = ListNode(0)
        new_head.next = head
        queue = []
        while cursor:
            queue.append(cursor)
            if len(queue) > n + 1:
                queue.pop(0)
            cursor = cursor.next
        previous = queue.pop(0)
        to_del = queue.pop(0)
        previous.next = to_del.next
        return new_head.next
        # cursor = new_head = ListNode(0)
        # new_head.next = head
        # stack = []
        # while cursor:
        #     stack.append(cursor)
        #     cursor = cursor.next
        # while n > 1:
        #     stack.pop()
        #     n = n - 1
        # to_del = stack.pop()
        # previous = stack.pop()
        # previous.next = to_del.next
        # return new_head.next


def main():
    sol = Solution()
    root = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    root.next = n2
    n2.next = n3
    n3.next = n4
    sol.removeNthFromEnd(root, 1)
    while root:
        print "%s -> " % root.val,
        root = root.next
    print " End"


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
